import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('real_estate_model.pkl', 'rb'))

# Load columns
columns = pickle.load(open('columns.pkl', 'rb'))

st.set_page_config(page_title="Real Estate Price Prediction")

st.markdown(
    "<h1 style='text-align:center;color:green;'>🏠 Real Estate Price Prediction</h1>",
    unsafe_allow_html=True
)

st.write("Predict House Prices Based on Location")

# Inputs
total_sqft = st.number_input("Total Square Feet", min_value=300.0)

bath = st.number_input("Bathrooms", min_value=1)

balcony = st.number_input("Balconies", min_value=0)

bhk = st.number_input("BHK", min_value=1)

# Example locations
locations = [
    'Whitefield',
    'Indira Nagar',
    'Electronic City',
    'Marathahalli',
    'other'
]

selected_location = st.selectbox(
    "Select Location",
    locations
)

# Area types
area_types = [
    'Built-up Area',
    'Plot Area',
    'Super built-up Area'
]

selected_area = st.selectbox(
    "Area Type",
    area_types
)

if st.button("Predict Price"):

    input_data = pd.DataFrame(
        np.zeros((1, len(columns))),
        columns=columns
    )

    # Numeric values
    input_data['total_sqft'] = total_sqft
    input_data['bath'] = bath
    input_data['balcony'] = balcony
    input_data['bhk'] = bhk

    # price_per_sqft feature
    input_data['price_per_sqft'] = 5000

    # Location encoding
    location_col = 'location_' + selected_location

    if location_col in input_data.columns:
        input_data[location_col] = 1

    # Area type encoding
    area_col = 'area_type_' + selected_area

    if area_col in input_data.columns:
        input_data[area_col] = 1

    # Prediction
    prediction = model.predict(input_data)[0]

    st.success(f"Estimated House Price: ₹ {prediction:.2f} Lakhs")