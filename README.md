# churn_prediction
🎯 Predict telecom customer churn using a trained machine learning model with an interactive and beautifully designed Streamlit web app.
🚀 Project Setup & Usage (All Steps in One)
markdown
Copy
Edit
## 🚀 Project Setup & Usage

Follow the steps below to set up and run the Customer Churn Prediction web app:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Soniya-26/churn_prediction
   cd churn_prediction
Create and Activate a Virtual Environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux
Install the Required Packages

bash
Copy
Edit
pip install -r requirements.txt
Train the Model (only once)

If random_forest_model.joblib is already provided, skip this.

bash
Copy
Edit
python app.py
Run the Streamlit App

bash
Copy
Edit
streamlit run churn.py
View the App

Open the link provided in your terminal (usually http://localhost:8501)

Enter customer details and get instant churn prediction.
