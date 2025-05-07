
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("Delhi House Price Predictor")

# User inputs
location = st.selectbox("Location", ["South Delhi", "Rohini", "Connaught Place", "Hauz Khas", "Chandni Chowk"])
size = st.number_input("Size (sq ft)", min_value=200.0, max_value=10000.0, value=1500.0)
green_area = st.selectbox("Green Area", ["Low", "Medium", "High"])
amenities = st.selectbox("Nearby Amenities", ["Few", "Moderate", "Many"])
crime_rate = st.selectbox("Crime Rate", ["Low", "Medium", "High"])

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "Location": location,
        "Size (sq ft)": size,
        "Green Area": green_area,
        "Nearby Amenities": amenities,
        "Crime Rate": crime_rate
    }])
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Price: ₹{int(prediction):,}")
