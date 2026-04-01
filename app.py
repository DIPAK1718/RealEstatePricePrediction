import streamlit as st
import pickle
import json
import numpy as np

# Load model
model = pickle.load(open("real_estate_model.pkl", "rb"))

# Load columns
with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']

# Locations start after first 3 columns
locations = data_columns[3:]

st.title("🏠 Real Estate Price Prediction")

st.write("Enter property details below")

# Inputs
sqft = st.number_input("Total Square Feet", min_value=300.0, value=1000.0)
bath = st.number_input("Number of Bathrooms", min_value=1, value=2)
bhk = st.number_input("BHK", min_value=1, value=2)

location = st.selectbox("Location", locations)

# Prediction
if st.button("Predict Price"):

    x = np.zeros(len(data_columns))

    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    prediction = model.predict([x])[0]

    st.success(f"Estimated Price: ₹ {round(prediction,2)} Lakhs")