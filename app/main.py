from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

model = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
scaler = joblib.load("scaler.pkl")

app = FastAPI()

class CropInput(BaseModel):
    N: int
    P: int
    K: int
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@app.post("/predict")
def predict_crop(data: CropInput):
    input_df = pd.DataFrame([data.model_dump()])
    scaled_input = scaler.transform(input_df)
    pred = model.predict(scaled_input)[0]
    crop_name = label_encoder.inverse_transform([pred])[0]
    return {"predicted_crop": crop_name}
