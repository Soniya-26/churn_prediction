
import streamlit as st
from joblib import load

# Load the trained Random Forest model (make sure this file exists)
model = load('random_forest_model.joblib')

st.title("Customer Churn Prediction App")

# Input fields
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=1)
internet_service = st.selectbox("Internet Service", ('DSL', 'Fiber optic', 'No'))
contract = st.selectbox("Contract", ('Month-to-month', 'One year', 'Two year'))
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=0.0)

# Mapping categorical inputs to numbers (must match encoding in training)
label_mapping = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2,
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2,
}
internet_service_encoded = label_mapping[internet_service]
contract_encoded = label_mapping[contract]

if st.button("Predict Churn"):
    # Prepare input in correct order as a 2D array for prediction
    input_data = [[tenure, internet_service_encoded, contract_encoded, monthly_charges, total_charges]]

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.success("✅ This customer is likely to stay.")
    else:
        st.error("⚠️ This customer is likely to churn.")
