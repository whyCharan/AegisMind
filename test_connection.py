import sys
import os
from components.logging.logger import logging  

# ENSURE WE CAN IMPORT FROM components
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from components.database.mysql_client import get_connection
from dotenv import load_dotenv

# RE-LOAD ENV VARS TO BE SURE
load_dotenv(os.path.join(parent_dir, '.env'))

def test_connection():
    
        
    # CHECK IF ENV VARS ARE LOADED
    host = os.getenv('MYSQL_HOST')
    user = os.getenv('MYSQL_USER')
    password = os.getenv('MYSQL_PASSWORD')
    
    logging.info(f"Environment Variables Check:\n")
    logging.info(f"HOST: {host}\n")
    logging.info(f"USER: {user}\n")
    logging.info(f"PASSWORD: {'*' * len(password) if password else 'None'} (Length: {len(password) if password else 0})\n")

    try:
        connection = get_connection()
        if connection.is_connected():
            logging.info("SUCCESS: Connected to MySQL database!")
            logging.info(f"Server info: {connection.get_server_info()}\n")
            connection.close()
        else:
            logging.info("RETURNED: Connection object returned but is_connected() is False\n")
    except Exception as e:
        logging.info(f"FAILURE: Could not connect to database.\n")
        logging.info(f"Error: {e}\n")

if __name__ == "__main__":
    test_connection()
