
# 🏠 Boston House Price Prediction

This project is a Machine Learning-powered web application built with **Streamlit** that predicts housing prices in Boston based on various features such as number of rooms, crime rate, tax rate, etc.

## 🚀 Features

- Predict house prices using two models:
  - **Linear Regression**
  - **XGBoost Regressor**
- User-friendly Streamlit web interface
- Input sliders for features
- Real-time price prediction display

## 📁 Project Structure

```
house_price_prediction/
├── app/
│   └── app.py             # Streamlit frontend app
├── models/
│   ├── linear_model.pkl   # Trained Linear Regression model
│   └── xgb_model.pkl      # Trained XGBoost model
├── data/
│   └── housing.csv        # Boston housing dataset
├── training/
│   └── train_models.ipynb # Notebook for training models
└── README.md
```

## 📦 Requirements

Install all necessary packages using:

```bash
pip install streamlit pandas numpy matplotlib seaborn scikit-learn xgboost joblib
```

## ▶️ Run the App

Navigate to the project directory and run:

```bash
streamlit run app/app.py
```

Then open the local URL provided (usually http://localhost:8501) in your browser.

## 📊 Dataset

The project uses the **Boston Housing Dataset** available on Kaggle.

## 🧠 ML Models

- **Linear Regression:** Simple and interpretable baseline model.
- **XGBoost Regressor:** Powerful ensemble model for better accuracy.

## 📌 Author

Made with ❤️ by [Your Name]
