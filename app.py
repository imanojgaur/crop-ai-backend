import pickle
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

# 1. Initialize the FastAPI instance (ASGI application)
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

# 3. Load the AI Model into RAM once when the server starts
MODEL_PATH = 'Crop_Recommendation.pkl'
with open(MODEL_PATH, 'rb') as file:
    ml_model = pickle.load(file)

# 4. Define the POST Route Handler
@app.post("/predict")
def predict_crop(payload: CropPredictionRequest):
    
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
    
    # 5. Make the AI Prediction
    prediction = ml_model.predict(features)
    
    # 6. Return standard Python dictionary (FastAPI automatically converts to JSON)
    return {'recommended_crop': prediction[0]}