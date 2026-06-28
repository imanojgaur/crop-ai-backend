import pickle
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# 1. Initialize the FastAPI instance
app = FastAPI(title="Crop Recommendation AI API")

# 2. Define the Pydantic Data Validation Model
class CropPredictionRequest(BaseModel):
    N: float = Field(description="Nitrogen content in soil")
    P: float = Field(description="Phosphorous content in soil")
    K: float = Field(description="Potassium content in soil")
    temperature: float = Field(description="Temperature in Celsius")
    humidity: float = Field(description="Relative humidity in %")
    ph: float = Field(description="pH value of the soil")
    rainfall: float = Field(description="Rainfall in mm")

# 3. Load the AI Model into RAM once
MODEL_PATH = 'Crop_Recommendation2.pkl'
try:
    with open(MODEL_PATH, 'rb') as file:
        ml_model = pickle.load(file)
except FileNotFoundError:
    raise RuntimeError(f"CRITICAL ERROR: Model file {MODEL_PATH} not found. Did you run train.py?")

# 4. Define the POST Route Handler (Standard 'def' for CPU-bound threadpooling)
@app.post("/predict")
def predict_crop(payload: CropPredictionRequest):
    try:
        # Extract features in the correct order for Scikit-Learn
        features = np.array([[
            payload.N,
            payload.P,
            payload.K,
            payload.temperature,
            payload.humidity,
            payload.ph,
            payload.rainfall
        ]])
        
        # Make the AI Prediction
        prediction = ml_model.predict(features)
        
        return {'recommended_crop': prediction[0]}
        
    except Exception as e:
        # If ANYTHING goes wrong in the math or numpy, catch it here.
        # It throws a clean 500 error to the user and prints the exact python error message.
        raise HTTPException(
            status_code=500, 
            detail=f"The AI model encountered an internal error: {str(e)}"
        )