# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

model = joblib.load("app/random_forest_model.pkl")
label_encoder = joblib.load("app/label_encoder.pkl")
scaler = joblib.load("app/scaler.pkl")

class InputData(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.post("/predict")
def predict(data: InputData):
    input_array = np.array([[data.N, data.P, data.K, data.temperature, data.humidity, data.ph, data.rainfall]])
    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)
    crop_name = label_encoder.inverse_transform(prediction)[0]
    return {"prediction": crop_name}
