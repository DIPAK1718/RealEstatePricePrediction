# RealEstatePricePrediction
# Real Estate Price Prediction Using Machine Learning

## 📌 Project Overview
This project predicts house prices based on features such as location, total square feet, BHK, bathrooms, and balcony using Machine Learning techniques.

The project uses the Bengaluru Housing Dataset and implements data preprocessing, feature engineering, exploratory data analysis (EDA), model training, hyperparameter tuning, and deployment using Streamlit.

---

# 🚀 Features
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Outlier Detection & Removal
- Feature Engineering
- One-Hot Encoding
- Machine Learning Model Training
- Hyperparameter Tuning
- Streamlit Web Application
- Real-Time House Price Prediction

---

# 📊 Dataset
Dataset Used:
Bengaluru House Price Dataset

Dataset Source:
https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

---

# 🛠 Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle
- VS Code

---

# 📂 Project Structure

RealEstateProject/

│

├── Bengaluru_House_Data.csv

├── app.py

├── model_training.ipynb

├── real_estate_model.pkl

├── columns.json

├── requirements.txt

├── logbook.md

└── README.md

---

# ⚙️ Data Preprocessing Steps

## 1️⃣ Handling Missing Values
- Removed null values
- Filled missing bathroom and balcony values using median

## 2️⃣ Feature Engineering
- Converted size column into numeric BHK
- Converted total_sqft into numeric values
- Created price_per_sqft feature

## 3️⃣ Outlier Removal
Removed unrealistic records using:
- sqft per BHK filtering
- bathroom filtering
- price_per_sqft filtering

## 4️⃣ One-Hot Encoding
Applied One-Hot Encoding on location column.

---

# 📊 Exploratory Data Analysis (EDA)

Performed:
- Price Distribution Analysis
- BHK Distribution
- Location Analysis
- Correlation Heatmap
- Scatter Plots
- Outlier Detection using Boxplots

---

# 🤖 Machine Learning Models

## 1️⃣ Linear Regression
Baseline model used for comparison.

## 2️⃣ Random Forest Regressor
Final optimized model with improved performance.

---

# 📈 Model Performance

| Model | R² Score |
|---|---|
| Linear Regression | 0.75 |
| Random Forest | 0.80 |

---

# 🌐 Streamlit Web App

The project includes a Streamlit-based web application where users can:
- Enter house details
- Select property information
- Predict house prices instantly

Run the app using:

```bash
streamlit run app.py
