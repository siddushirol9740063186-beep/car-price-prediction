import streamlit as st
import numpy as np
import pickle
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Car Price Prediction", layout="centered")

st.title("🚗 Car Price Prediction")
st.write("Predict resale price of a car using Machine Learning")

# ---------------- LOAD MODEL SAFELY ----------------
MODEL_PATH = "model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ model.pkl file not found!")
    st.write("📂 Files available:", os.listdir())
    st.stop()

try:
    with open(MODEL_PATH, "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error("❌ Error loading model.pkl")
    st.write(e)
    st.stop()

# ---------------- INPUTS ----------------
st.subheader("Enter Car Details")

year = st.slider("Year of Purchase", 2000, 2025, 2015)
present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)
kms_driven = st.number_input("Kilometers Driven", 0, 300000, 50000)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Number of Owners", [0, 1, 2, 3])

# ---------------- ENCODING ----------------
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 1, "Automatic": 0}

car_age = 2025 - year

input_data = np.array([[present_price, kms_driven,
                        fuel_map[fuel],
                        seller_map[seller],
                        trans_map[transmission],
                        owner,
                        car_age]])

# ---------------- PREDICTION ----------------
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"💰 Estimated Price: ₹ {round(prediction[0], 2)} Lakhs")
    except Exception as e:
        st.error("❌ Prediction Error")
        st.write(e)

# ---------------- FOOTER ----------------
st.markdown("---")
st.write("Built with ❤️ using Streamlit")
