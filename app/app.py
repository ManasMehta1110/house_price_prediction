import os
import streamlit as st
import joblib
import numpy as np

# Set base path assuming this file is in /app/ and models are in /models/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
LR_MODEL_PATH = os.path.join(BASE_DIR, "models", "linear_model.pkl")
XGB_MODEL_PATH = os.path.join(BASE_DIR, "models", "xgb_model.pkl")

# Load models
lr_model, xgb_model = None, None

try:
    lr_model = joblib.load(LR_MODEL_PATH)
except Exception as e:
    st.error(f"❌ Linear Regression model not found at:\n`{LR_MODEL_PATH}`\n\n**Error:** {e}")

try:
    xgb_model = joblib.load(XGB_MODEL_PATH)
except Exception as e:
    st.error(f"❌ XGBoost model not found at:\n`{XGB_MODEL_PATH}`\n\n**Error:** {e}")

# App title
st.title("🏠 Boston House Price Predictor")

# Sidebar for model selection
model_choice = st.sidebar.selectbox("Choose Model", ["Linear Regression", "XGBoost"])

# Input form
st.header("Enter House Features")

CRIM = st.number_input("Crime Rate (CRIM)", min_value=0.0, value=0.1)
ZN = st.number_input("Residential Land (ZN)", min_value=0.0, value=0.0)
INDUS = st.number_input("Non-Retail Land (INDUS)", min_value=0.0, value=7.0)
CHAS = st.selectbox("Charles River (CHAS)", [0, 1])
NOX = st.number_input("Nitric Oxide Concentration (NOX)", min_value=0.0, max_value=1.0, value=0.5)
RM = st.number_input("Average Rooms (RM)", min_value=1.0, value=6.0)
AGE = st.number_input("Age of House (AGE)", min_value=0.0, value=65.0)
DIS = st.number_input("Distance to Employment (DIS)", min_value=0.0, value=4.0)
RAD = st.slider("RAD (Accessibility to Highways)", 1, 24, 5)
TAX = st.number_input("Property Tax Rate (TAX)", min_value=0.0, value=300.0)
PTRATIO = st.number_input("Pupil-Teacher Ratio (PTRATIO)", min_value=0.0, value=15.0)
B = st.number_input("B (1000(Bk - 0.63)^2)", min_value=0.0, value=390.0)
LSTAT = st.number_input("LSTAT (% Lower Status Population)", min_value=0.0, value=12.0)

# Predict
if st.button("Predict Price"):
    input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE,
                            DIS, RAD, TAX, PTRATIO, B, LSTAT]])

    if model_choice == "Linear Regression":
        if lr_model:
            prediction = lr_model.predict(input_data)[0]
            st.success(f"🏡 Estimated Price: **${prediction * 1000:,.2f}**")
        else:
            st.error("⚠️ Linear Regression model is not loaded.")
    
    elif model_choice == "XGBoost":
        if xgb_model:
            prediction = xgb_model.predict(input_data)[0]
            st.success(f"🏡 Estimated Price: **${prediction * 1000:,.2f}**")
        else:
            st.error("⚠️ XGBoost model is not loaded.")
