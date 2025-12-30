import pandas as pd
import sys
import os

# Create a robust path setup to allow running from src or root
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from src.database.mysql_client import get_connection
from src.exception.custom_exception import AegisMindException
from src.logger.logger import logging

def upload_csv_to_mysql(csv_file_path: str):
    try:
        logging.info("Starting the data ingestion process...")
        df = pd.read_csv(csv_file_path)

        if 'Unnamed: 0' in df.columns:
            df.drop(columns=['Unnamed: 0'], inplace=True)

        #Map labels
        if 'class' in df.columns:
            df['label'] = df['class'].map(
                {'suicide':1, 'non-suicide':0}
            )
            df.drop(columns=['class'], inplace=True)
        
        df.dropna(inplace=True)

        insert_query = """
        INSERT INTO suicide_messages(TEXT,LABEL)
        VALUES(%s,%s)
        """
        
        connection = get_connection()
        cursor = connection.cursor()
        
        try:
            data = [(row["text"], int(row["label"])) for _, row in df.iterrows()]
            
            batch_size = 1000
            for i in range(0, len(data), batch_size):
                batch = data[i:i + batch_size]
                cursor.executemany(insert_query, batch)
                connection.commit()
                logging.info(f"Inserted batch {i//batch_size + 1}: {len(batch)} records")
                
            logging.info("Data ingestion completed successfully.")
            logging.info(f"Inserted total {len(data)} records into MySQL")
        finally:
            cursor.close()
            connection.close()
        
        # Save to disk for DVC pipeline
        processed_dir = os.path.join(parent_dir, 'data', 'processed')
        os.makedirs(processed_dir, exist_ok=True)
        output_path = os.path.join(processed_dir, 'suicide_data.csv')
        df.to_csv(output_path, index=False)
        logging.info(f"Saved processed data to {output_path}")

    except Exception as e:
        raise AegisMindException(e, sys)

if __name__ == "__main__":
    
    csv_path = os.path.join(parent_dir, 'data', 'Suicide_Detection.csv')
    upload_csv_to_mysql(csv_path)
