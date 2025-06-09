import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from joblib import dump

# Load the dataset (make sure 'Telco_Customer_Churn.csv' is in your working directory)
telecom_cust = pd.read_csv('Telco_Customer_Churn.csv')

# Data preprocessing
# Convert 'TotalCharges' to numeric, replace errors with NaN, fill NaN with 0
telecom_cust['TotalCharges'] = pd.to_numeric(telecom_cust['TotalCharges'], errors='coerce')
telecom_cust['TotalCharges'].fillna(0, inplace=True)

# Convert 'Churn' to binary labels (0 = stay, 1 = churn)
label_encoder = LabelEncoder()
telecom_cust['Churn'] = label_encoder.fit_transform(telecom_cust['Churn'])

# Use Label Encoding for categorical features
telecom_cust['InternetService'] = label_encoder.fit_transform(telecom_cust['InternetService'])
telecom_cust['Contract'] = label_encoder.fit_transform(telecom_cust['Contract'])

# Select features and target
selected_features = ['tenure', 'InternetService', 'Contract', 'MonthlyCharges', 'TotalCharges']
X = telecom_cust[selected_features]
y = telecom_cust['Churn']

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=101)
model.fit(X, y)

# Save the trained model to a file
dump(model, 'random_forest_model.joblib')

print("Model training complete and saved as 'random_forest_model.joblib'.")













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
