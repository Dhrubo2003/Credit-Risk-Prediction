# Credit Risk Prediction

## Overview
The **Credit Risk Prediction** project aims to predict the credit risk of individuals using a machine learning model based on the Statlog German Credit dataset. The model utilizes XGBoost for classification and is deployed as a web application using Streamlit. Users can input personal and financial information to receive a risk assessment.

## Features
- Predict credit risk using a trained XGBoost model.
- User-friendly web interface powered by Streamlit.
- Hyperparameter tuning performed using GridSearchCV to optimize model performance.

## Project Structure

```plaintext
credit-risk-prediction/
├── README.md                 # Project overview and setup instructions
├── requirements.txt          # Python dependencies
├── src/
│   ├── main.py               # Streamlit app entry point
│   ├── lib/
│   │   └── model.py          # Code to load and use the model
│   └── tests/
│       └── test_model.py     # Unit tests for your model
├── dataset/
│   └── german.data           # Dataset used for training
