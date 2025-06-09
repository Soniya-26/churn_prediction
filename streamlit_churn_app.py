import streamlit as st
import pandas as pd
from joblib import load

# Load model
model = load('random_forest_model.joblib')
st.markdown(
    """
    <style>
    .main {
        background-color: white;
        padding: 2rem;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        color: royalblue;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subtitle {
        color: white;
        font-size: 1.2rem;
        margin-bottom: 20px;
    }
    .result {
        font-size: 1.3rem;
        font-weight: bold;
        padding: 1rem;
        border-radius: 10px;
    }
    /* Custom styles for input labels */
    label[data-baseweb="select"], 
    label[data-baseweb="number"] {
        background-color: #87CEEB; /* sky blue */
        color: black !important;
        padding: 6px 10px;
        border-radius: 5px;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 6px;
    }
    /* Slider marks (numbers) color */
    div[data-baseweb="slider"] > div:first-child > div > div > div {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown('<div class="title">📊 Customer Churn Prediction</div>', unsafe_allow_html=True)

st.markdown('<p class="subtitle">Fill in customer details below to see if they are likely to churn.</p>', unsafe_allow_html=True)

# Input fields
tenure = st.slider("📅 Tenure (in months)", 0, 72, 12)
internet_service = st.selectbox("🌐 Internet Service", ('DSL', 'Fiber optic', 'No'))
contract = st.selectbox("📄 Contract Type", ('Month-to-month', 'One year', 'Two year'))
monthly_charges = st.number_input("💵 Monthly Charges", min_value=0.0, value=50.0)
total_charges = st.number_input("💰 Total Charges", min_value=0.0, value=1000.0)

# Map categorical inputs to numeric
label_mapping = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2,
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2,
}

internet_service_val = label_mapping[internet_service]
contract_val = label_mapping[contract]

if st.button("Predict Churn"):
    X_input = preprocess_input()
    X_scaled = scaler.transform(X_input)  # scaler expects 2D array
    prediction = model.predict(X_scaled)[0]

    if prediction == 1:
        st.markdown('<p style="color: black; font-weight: bold;">⚠️ The customer is likely to churn.</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p style="color: black; font-weight: bold;">✅ The customer is likely to stay.</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
