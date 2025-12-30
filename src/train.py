import os
import pandas as pd
import numpy as np
import pickle
import nltk
import mlflow
import mlflow.tensorflow
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Import components
# Assuming running from root directory
import sys
sys.path.append(os.getcwd())

from src.logger.logger import logger
from src.preprocessing import clean
from src.tokenizer import fit_tokenizer, save_tokenizer
from src.model import build_model

def train_pipeline(data_path, models_dir='models', sample_size=None):
    # Ensure NLTK resources
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('punkt')
    nltk.download('punkt_tab')

    logger.info("Loading data...")
    df = pd.read_csv(data_path)
    
    # Use subset for faster training demonstration
    if sample_size and len(df) > sample_size:
        logger.info(f"Using a subset of {sample_size} samples...")
        df = df.sample(sample_size, random_state=42)
    
    # Preprocessing
    logger.info("Cleaning text...")
    df['cleaned_text'] = df['text'].apply(clean)
    
    # Prepare target
    logger.info("Preparing target...")
    if 'class' in df.columns:
        df['label'] = df['class'].map({'suicide': 1, 'non-suicide': 0})
    else:
        logger.info("Warning: 'class' column not found, checking for 'label'...")
        pass

    # Tokenization
    logger.info("Fitting tokenizer...")
    max_words = 10000
    max_len = 100
    tokenizer = fit_tokenizer(df['cleaned_text'], max_words=max_words)
    
    os.makedirs(models_dir, exist_ok=True)
    save_tokenizer(tokenizer, os.path.join(models_dir, 'tokenizer.pkl'))
    
    sequences = tokenizer.texts_to_sequences(df['cleaned_text'])
    X = pad_sequences(sequences, maxlen=max_len, padding='post', truncating='post')
    y = df['label'].values
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Build Model
    logger.info("Building model...")
    model = build_model(vocab_size=max_words+1, max_length=max_len)
    
    # Train
    logger.info("Training model...")
    checkpoint = ModelCheckpoint(os.path.join(models_dir, 'aegismind_model.keras'), monitor='val_accuracy', save_best_only=True, mode='max')
    early_stop = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    
    # MLflow tracking
    mlflow.set_experiment("AegisMind Experiment")
    
    with mlflow.start_run():
        params = {
            "epochs": 5,
            "batch_size": 32,
            "vocab_size": max_words,
            "max_len": max_len
        }
        mlflow.log_params(params)
        
        history = model.fit(
            X_train, y_train,
            validation_data=(X_test, y_test),
            epochs=5,
            batch_size=32,
            callbacks=[checkpoint, early_stop]
        )
        
        # Log metrics
        for metric, values in history.history.items():
            mlflow.log_metric(metric, values[-1])
            
        # Log model
        mlflow.tensorflow.log_model(model, "model")
        
        logger.info("Training complete and logged to MLflow.")
        
    return history


if __name__ == "__main__":
    data_path = os.path.join('data', 'processed', 'suicide_data.csv')
    train_pipeline(data_path)
