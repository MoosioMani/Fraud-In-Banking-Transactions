import os
import numpy as np
import joblib
import streamlit as st

def render():
    st.title("Fraud Detection System")
    st.markdown("Please enter the transaction details:")

model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../model/lightgbm_model.pkl'))
encoders_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'encoders.pkl'))

if not os.path.exists(model_path):
    st.error(f"Model file not found! Path: {model_path}")
    st.stop()

if not os.path.exists(encoders_path):
    st.error(f"Encoder file not found! Path: {encoders_path}")
    st.stop()

model = joblib.load(model_path)
encoders = joblib.load(encoders_path)

categorical_features = ["Transaction_ID", "User_ID","Transaction_Type", "Device_Type", "Location", "Merchant_Category",
    "Card_Type", "Authentication_Method"]
numeric_features = ['Transaction_Amount', 'Account_Balance', 'IP_Address_Flag', 'Previous_Fraudulent_Activity',
                    'Card_Age', 'Transaction_Distance', 'Risk_Score', 'Is_Weekend', 'hour', 'day_of_week', 
                    'day_of_month', 'month', 'is_night', 'Transaction_Ratio', 'Failed_Transaction_Rate']


user_input = {}

for feature in numeric_features:
    user_input[feature] = st.number_input(f"{feature}", value=0.0)

for feature in categorical_features:
    val = st.text_input(f"{feature}", key=f"text_{feature}")
    if val.strip() == "":
        st.warning(f"Please enter a value for {feature}.")
        continue
    try:
        encoded_value = encoders[feature].transform([val])[0]
    except Exception:
        st.warning(f"Unknown value '{val}' for {feature}, setting to -1")
        encoded_value = -1
    user_input[feature] = encoded_value

if st.button("Predict"):
    try:
        input_features = [user_input[feature] for feature in numeric_features + categorical_features]
        input_array = np.array([input_features])
        prediction = model.predict(input_array)
        if prediction[0] == 1:
            st.warning("This transaction is suspected of fraud!")
        else:
            st.success("This transaction is legitimate.")
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")