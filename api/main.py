from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import os
import sys

# Add root to sys path to import components
sys.path.append(os.getcwd())
from src.preprocessing import clean

app = FastAPI(title="AegisMind API", description="Suicide Ideation Detection API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Global variables for model and tokenizer
model = None
tokenizer = None
MAX_LEN = 100

class PredictionRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float

@app.on_event("startup")
async def load_artifacts():
    global model, tokenizer
    try:
        model_path = os.path.join("models", "aegismind_model.keras")
        tokenizer_path = os.path.join("models", "tokenizer.pkl")
        
        if os.path.exists(model_path) and os.path.exists(tokenizer_path):
            model = load_model(model_path)
            with open(tokenizer_path, 'rb') as handle:
                tokenizer = pickle.load(handle)
            print("Model and Tokenizer loaded successfully.")
        else:
            print("Model or Tokenizer not found. Please train the model first.")
    except Exception as e:
        print(f"Error loading model: {e}")

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    if model is None or tokenizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    # Preprocess
    cleaned_text = clean(request.text)
    
    # Tokenize
    sequences = tokenizer.texts_to_sequences([cleaned_text])
    padded = pad_sequences(sequences, maxlen=MAX_LEN, padding='post', truncating='post')
    
    # Predict
    prediction_prob = model.predict(padded)[0][0]
    
    label = "Suicide" if prediction_prob > 0.5 else "Non-Suicide"
    
    return {
        "prediction": label,
        "confidence": float(prediction_prob)
    }

@app.get("/")
def read_root():
    return {"message": "AegisMind API is running"}
