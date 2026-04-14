import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="Car Price Prediction")

# ----------- CHECK MODEL FILE -----------
if not os.path.exists("model.pkl"):
    st.error("❌ model.pkl not found! Run training first.")
    st.stop()

model = pickle.load(open("model.pkl", "rb"))

# ----------- UI DESIGN -----------
st.markdown("## 🚗 Car Price Prediction")
st.write("Predict car resale price using ML")

st.markdown("### Enter Car Details")

year = st.slider("Year of Purchase", 2000, 2025, 2015)
present_price = st.number_input("Present Price (Lakhs)", 0.0, 50.0, 5.0)
kms_driven = st.number_input("Kilometers Driven", 0, 300000, 50000)

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owners", [0, 1, 2, 3])

# ----------- ENCODING (MUST MATCH TRAINING) -----------
fuel_map = {"Petrol": 2, "Diesel": 1, "CNG": 0}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 1, "Automatic": 0}

car_age = 2025 - year

input_data = np.array([[present_price, kms_driven, fuel_map[fuel],
                        seller_map[seller], trans_map[transmission],
                        owner, car_age]])

# ----------- PREDICTION -----------
if st.button("Predict"):
    result = model.predict(input_data)
    st.success(f"💰 Estimated Price: ₹ {round(result[0], 2)} Lakhs")

st.markdown("---")
st.write("Built with ❤️ using Streamlit")
