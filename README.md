# 🏠 Real Estate Price Prediction Using Machine Learning

## 📌 Project Overview

This project predicts house prices based on features such as location, total square feet, BHK, bathrooms, and balcony using Machine Learning techniques.

The project uses the Bengaluru Housing Dataset and implements data preprocessing, feature engineering, exploratory data analysis (EDA), model training, model comparison, and deployment using Streamlit.  

---  

# 🚀 Features  
 
* Data Cleaning & Preprocessing  
* Exploratory Data Analysis (EDA)
* Missing Value Handling  
* Outlier Detection & Removal   
* Feature Engineering   
* One-Hot Encoding
* Machine Learning Model Training 
* Model Comparison
* Streamlit Web Application
* Real-Time House Price Prediction 

---

# 📊 Dataset

### Dataset Used

Bengaluru House Price Dataset

### Dataset Source

https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data

### Dataset Features

| Feature      | Description                   |
| ------------ | ----------------------------- |
| area_type    | Type of property area         |
| availability | Availability status           |
| location     | Property location             |
| size         | House size (BHK)              |
| society      | Society name                  |
| total_sqft   | Total area in square feet     |
| bath         | Number of bathrooms           |
| balcony      | Number of balconies           |
| price        | House price (Target Variable) |

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Pickle
* VS Code

---

# 📂 Project Structure

```text
RealEstateProject/

│

├── Bengaluru_House_Data.csv

├── app.py

├── model.ipynb

├── real_estate_model.pkl

├── columns.pkl

├── requirements.txt

├── screenshots/

├── logbook.md

└── README.md
```

---

# ⚙️ Data Preprocessing Steps

## 1️⃣ Handling Missing Values

* Removed null values
* Filled missing bathroom values using median
* Filled missing balcony values using median

## 2️⃣ Feature Engineering

* Converted size column into numeric BHK
* Converted total_sqft into numeric values
* Created price_per_sqft feature
* Reduced rare locations into "other"

## 3️⃣ Outlier Removal

Removed unrealistic records using:

* Square feet per BHK filtering
* Bathroom filtering
* Price per square feet filtering

## 4️⃣ One-Hot Encoding

Applied One-Hot Encoding on:

* location
* area_type

---

# 📊 Exploratory Data Analysis (EDA)

We Performed the following analyses:

### Price Distribution Analysis

Understanding the distribution of house prices.

### Area Type Distribution

Analyzing different property area types.

### Location Analysis

Finding the most popular property locations.

### BHK Distribution

Understanding the distribution of house sizes.

### Bathroom & Balcony Analysis

Analyzing amenities available in properties.

### Area vs Price Analysis

Studying the relationship between area and house price.

### Correlation Heatmap

Identifying relationships between numerical features.

### Outlier Detection

Detecting unusual property records using boxplots.

---

# 🤖 Machine Learning Models

## 1️⃣ Linear Regression

Baseline model used for comparison.

## 2️⃣ Decision Tree Regressor

Used to capture non-linear relationships.

## 3️⃣ Random Forest Regressor

Improved accuracy through ensemble learning.

## 4️⃣ Gradient Boosting Regressor

Boosting-based regression model.

---

# 📈 Model Performance

| Model             | R² Score |
| ----------------- | -------- |
| Linear Regression | 0.86     |
| Decision Tree     | 0.94     |
| Random Forest     | 0.99     |
| Gradient Boosting | 0.997    |


### 🏆 Best Model

**Gradient Boosting**

> Note: Scores may vary depending on preprocessing, train-test split, and hyperparameter tuning.

---

# 🌐 Streamlit Web App

The project includes a Streamlit-based web application where users can:

* Enter house details
* Select property information
* Predict house prices instantly
* View estimated property price

Run the application using:

```bash
streamlit run app.py
```

Application URL:

```text
http://localhost:8501
```

---

# 🎯 Applications

* Real Estate Agencies
* Property Dealers
* Housing Portals
* Property Investors
* Home Buyers

---

# Future Enhancements

* Live Property Data Integration
* Map-Based Location Selection
* Cloud Deployment
* Mobile Application
* Deep Learning Models
* Property Recommendation System

---
