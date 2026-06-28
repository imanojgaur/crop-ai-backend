import os 
import pickle
import numpy as np
from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# load .env local system.
load_dotenv()

app = FastAPI(title="Crop Recommendation AI API")

# Fetch or Fallback to None 
EXPECTED_API_KEY = os.getenv("CROP_BACKEND_SECRET_KEY")

if not EXPECTED_API_KEY:
    raise RuntimeError("CRITICAL: CROP_BACKEND_SECRET_KEY environment variable is not set!")

# Data Validation Model
class CropPredictionRequest(BaseModel):
    N: float = Field(description="Nitrogen content in soil")
    P: float = Field(description="Phosphorous content in soil")
    K: float = Field(description="Potassium content in soil")
    temperature: float = Field(description="Temperature in Celsius")
    humidity: float = Field(description="Relative humidity in %")
    ph: float = Field(description="pH value of the soil")
    rainfall: float = Field(description="Rainfall in mm")

# Load ai
MODEL_PATH = 'Crop_Recommendation2.pkl'
try:
    with open(MODEL_PATH, 'rb') as file:
        ml_model = pickle.load(file)
except FileNotFoundError:
    raise RuntimeError(f"CRITICAL ERROR: Model file {MODEL_PATH} not found. Did you run train.py?")


# The Security Bouncer Function              |fallback
def verify_api_key(x_api_key: str = Header(None, alias="x-api-key")):
    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(
            status_code=401, 
            detail="Unauthorized. Missing or invalid API key."
        )
    return x_api_key

# handle next.js DAP req only.
@app.post("/predict", dependencies=[Depends(verify_api_key)])
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
        
        # Make AI Prediction
        prediction = ml_model.predict(features)
        
        return {'recommended_crop': prediction[0]}
        
    except Exception as e:
        # If ANYTHING goes wrong in the math or numpy, catch it here.
        raise HTTPException(
            status_code=500, 
            detail=f"The AI model encountered an internal error: {str(e)}"
        )