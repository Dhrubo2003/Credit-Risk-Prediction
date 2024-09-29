import streamlit as st
import pickle
import numpy as np


# Load your trained model
model = pickle.load(open('credit_scoring_model.pkl', "rb"))

# Set the title of the app
st.title("Credit Scoring Model")

# Input fields for the features used in the model
st.write("Please enter the following information:")

# Example input fields
age = st.number_input("Age", min_value=0, max_value=120)
credit_amount = st.number_input("Credit Amount", min_value=0)
loan_duration = st.number_input("Loan Duration (in months)", min_value=0)

# Handle categorical inputs: using numerical encoding or label encoding
employment_status = st.selectbox("Employment Status", options=["Employed", "Unemployed", "Self-Employed"])
housing_status = st.selectbox("Housing Status", options=["Own", "Rent", "Free"])

# Convert categorical features to numeric format based on your encoding
employment_mapping = {"Employed": 1, "Unemployed": 0, "Self-Employed": 2}
housing_mapping = {"Own": 1, "Rent": 0, "Free": 2}

# Encode the inputs
employment_encoded = employment_mapping[employment_status]
housing_encoded = housing_mapping[housing_status]

# Button to make prediction
if st.button("Predict"):
    # Create the feature array
    features = np.array([[age, credit_amount, loan_duration, employment_encoded, housing_encoded]])
    
    # Make prediction
    prediction = model.predict(features)
    st.write(f"Prediction: {int(prediction[0])}")  # Show prediction
