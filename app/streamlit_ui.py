import streamlit as st
import joblib
import pandas as pd

# Load model and encoder
model = joblib.load("random_forest_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
scaler = joblib.load("scaler.pkl")  # Load the scaler

st.set_page_config(page_title="Crop Predictor", layout="centered")

st.title("🌾 Crop Prediction App")
st.markdown("Enter soil and climate parameters below to predict the most suitable crop.")

# Input sliders
N = st.slider("Nitrogen (N)", 0, 150, 90)
P = st.slider("Phosphorus (P)", 0, 150, 42)
K = st.slider("Potassium (K)", 0, 200, 43)
temperature = st.slider("Temperature (°C)", 0.0, 50.0, 22.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 80.0)
ph = st.slider("Soil pH", 0.0, 14.0, 6.5)
rainfall = st.slider("Rainfall (mm)", 0.0, 300.0, 200.0)

if st.button("Predict Crop"):
    input_data = pd.DataFrame([{
        "N": N,
        "P": P,
        "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }])
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)[0]
    predicted_crop = label_encoder.inverse_transform([prediction])[0]
    st.success(f"✅ Recommended Crop: **{predicted_crop}**")
