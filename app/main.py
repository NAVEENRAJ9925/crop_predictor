# app/main.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

model = joblib.load(os.environ.get("MODEL_PATH"))
scaler = joblib.load(os.environ.get("SCALER_PATH"))
label_encoder = joblib.load(os.environ.get("ENCODER_PATH"))

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
