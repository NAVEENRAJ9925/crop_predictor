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
from fastapi import Request
from fastapi.responses import Response
import httpx

@app.get("/streamlit/{path:path}")
async def proxy_streamlit(request: Request, path: str):
    url = f"http://localhost:8501/{path}"
    headers = dict(request.headers)
    async with httpx.AsyncClient() as client:
        response = await client.request(
            request.method, url, headers=headers, content=await request.body()
        )
    return Response(
        content=response.content,
        status_code=response.status_code,
        headers=dict(response.headers),
    )

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}
