import streamlit as st
import pickle
import numpy as np

# Step 1: Load the saved XGBoost model
with open('credit_scoring_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Step 2: Define the Streamlit inputs
st.title("Credit Risk Prediction")

# Take inputs from the user
age = st.number_input("Age", min_value=18, max_value=100, value=25)
credit_amount = st.number_input("Credit Amount", min_value=100, value=1000)
loan_duration = st.number_input("Loan Duration (in months)", min_value=6, max_value=72, value=12)

# Employment status select box
employment_status = st.selectbox("Employment Status", options=["Unemployed", "< 1 year", "1 - 4 years", "4 - 7 years", ">= 7 years"])
employment_mapping = {"Unemployed": 0, "< 1 year": 1, "1 - 4 years": 2, "4 - 7 years": 3, ">= 7 years": 4}
employment_encoded = employment_mapping[employment_status]

# Housing status select box
housing_status = st.selectbox("Housing Status", options=["Rent", "Own", "Free"])
housing_mapping = {"Rent": 0, "Own": 1, "Free": 2}
housing_encoded = housing_mapping[housing_status]

# Step 3: Prepare the input for the model
input_data = np.array([[age, credit_amount, loan_duration, employment_encoded, housing_encoded]])

# Step 4: Make predictions
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 0:
        st.write("Prediction: Low Risk")
    else:
        st.write("Prediction: High Risk")

