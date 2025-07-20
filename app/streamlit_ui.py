# app/streamlit_ui.py
import streamlit as st
import requests

st.title("🌾 Crop Recommendation System")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)
temperature = st.number_input("Temperature (°C)", format="%.2f")
humidity = st.number_input("Humidity (%)", format="%.2f")
ph = st.number_input("Soil pH", format="%.2f")
rainfall = st.number_input("Rainfall (mm)", format="%.2f")

if st.button("Predict Best Crop"):
    input_data = {
        "N": N, "P": P, "K": K,
        "temperature": temperature,
        "humidity": humidity,
        "ph": ph,
        "rainfall": rainfall
    }

    try:
        response = requests.post("http://localhost:8000/predict", json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"🌱 Recommended Crop: **{result['prediction']}**")
        else:
            st.error("🚫 Prediction failed.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
