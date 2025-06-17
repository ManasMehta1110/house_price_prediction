# 🏠 Boston House Price Prediction

A web application that predicts Boston house prices using machine learning models. Built with **Python**, **Streamlit**, and trained using the **Boston Housing Dataset**, the app allows users to enter housing details and get instant price predictions powered by **Linear Regression** and **XGBoost**.

## 🔗 Live Demo

- 🌐 [Try the App on Streamlit](https://housepriceprediction-yswxrns87rcg2mwdpxnyq8.streamlit.app/)
- 📂 [GitHub Repository](https://github.com/ManasMehta1110/house_price_prediction)

## 🚀 Features

- 🔍 Predict house prices using two models:
  - **Linear Regression**
  - **XGBoost Regressor**
- 🧠 Real-time predictions with Streamlit
- 🎛️ Interactive sliders and inputs for house features
- 📊 Clean, user-friendly interface

## 📁 Project Structure



```
house_price_prediction/
├── app/
│ └── app.py # Streamlit frontend app
├── models/
│ ├── linear_model.pkl # Trained Linear Regression model
│ └── xgb_model.pkl # Trained XGBoost model
├── data/
│ └── housing.csv # Boston housing dataset
├── training/
│ └── train_models.ipynb # Jupyter notebook for model training
├── requirements.txt # Required Python packages
├── .gitignore # Ignored files and folders
└── README.md
```

## 📦 Installation

Install all the required packages using:

```bash
pip install -r requirements.txt
```

## ▶️ Run the App

Navigate to the project directory and run:

```bash
cd house_price_prediction
streamlit run app/app.py
```

Then open the local URL provided (usually http://localhost:8501) in your browser.

## 📊 Dataset

The project uses the **Boston Housing Dataset** available on Kaggle.

## 🧠 ML Models

- **Linear Regression:** Simple and interpretable baseline model.
- **XGBoost Regressor:** Powerful ensemble model for better accuracy.

## 📌 Author

Made with ❤️ by Manas Mehta

📬 Feedback  
Have suggestions or feedback? Feel free to open an issue or [connect with me on LinkedIn](https://www.linkedin.com/in/manas-mehta-299b31314).
