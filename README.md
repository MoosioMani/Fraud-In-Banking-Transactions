# 💳 Fraud Detection System

A **Machine Learning-powered web application** for intelligent fraud detection in financial transactions, built with [Streamlit](https://streamlit.io/) and Python. This project demonstrates how to preprocess transaction data, train a robust model, and serve predictions through a modern, interactive UI.

---

## 🚀 Features

- **Real-time Fraud Prediction:** Instantly assess the risk of new transactions.
- **Modern UI:** User-friendly interface built with Streamlit.
- **Customizable Inputs:** Accepts both numerical and categorical transaction features.
- **Robust Error Handling:** Clear feedback for missing model files or incorrect inputs.
- **Easily Extendable:** Designed for integration with new features and models.

---

## 📁 Project Structure

```plaintext
project-root/
│
├── data/
│   └── fraud_dataset_mod.csv                        # Dataset
│
├── model/
│   └── lightgbm_model.pkl           # Trained LightGBM model
│
├── notebooks/
│   └── Final.ipynb                        # Jupyter Notebook File
│
├── ui/
│   └── ui.py                        # Streamlit UI for prediction
│
├── main.py                          # (Optional) Entry point for launching the app
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 🧑‍💻 How It Works

1. **Preprocessing:** Transaction data is cleaned and processed. Categorical features (like card type, device type, etc.) are label-encoded to match model expectations.
2. **Model Training:** A LightGBM model is trained using key features such as transaction amount, user account balance, transaction type, device, risk score, and more.
3. **Prediction:** The UI collects user inputs, applies necessary encodings, and feeds them to the model for live fraud prediction.

---

## 📝 Example Input Features

| Feature Name                   | Type      | Example Value     | Description                          |
|------------------------------- |-----------|------------------|--------------------------------------|
| Transaction_Amount             | float     | 1500.50          | Amount of transaction                |
| Account_Balance                | float     | 20000.00         | User's account balance               |
| IP_Address_Flag                | float     | 1.0              | IP address anomaly indicator         |
| Previous_Fraudulent_Activity   | float     | 0.0              | Previous fraud flag                  |
| Daily_Transaction_Count        | float     | 5.0              | Number of transactions today         |
| Avg_Transaction_Amount_7d      | float     | 1200.00          | 7-day average transaction amount     |
| Failed_Transaction_Count_7d    | float     | 1.0              | Failed transactions in last 7 days   |
| Card_Age                       | float     | 2.5              | Card age in years                    |
| Transaction_Distance           | float     | 10.0             | Distance from user's location (km)   |
| Risk_Score                     | float     | 0.75             | Risk score assigned to transaction   |
| Is_Weekend                     | float     | 1.0              | 1 if weekend, else 0                 |
| Card_Type                      | string    | "visa"           | Type of card used                    |
| Device_Type                    | string    | "mobile"         | Device used for transaction          |
| Transaction_Type               | string    | "purchase"       | Transaction category                 |
| ...                            | ...       | ...              | Extend as needed                     |

*Note: Categorical features must be encoded as per the training pipeline.*

---

## ⚡️ Quickstart

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 2. Place Your Trained Model

Ensure your trained model file (`lightgbm_model.pkl`) is in the `model/` directory.

### 3. Run the App

```bash
streamlit run main.py
```

---

## 🛠️ Customization

- **Feature Engineering:** Update the feature list and preprocessing steps in both the model pipeline and `ui.py`.
- **Model Replacement:** Swap in any scikit-learn-compatible model by saving it as `lightgbm_model.pkl`.
- **UI Enhancement:** Use Streamlit widgets (dropdowns, sliders, etc.) for better user experience.

---

## 📚 Tips & Best Practices

- Always preprocess and encode user inputs **exactly as during model training**.
- Keep categorical value mappings (e.g., label encoding for card types) consistent between training and inference.
- For new features, update both your model pipeline and Streamlit UI.
- Use environment variables or config files for sensitive paths and settings in production.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or improve.

---

## ⚖️ License

Distributed under the [MIT License](LICENSE).  
Copyright © 2025 [MoosioMani](https://github.com/MoosioMani)

---

## 💡 Inspiration

Inspired by real-world needs for secure, transparent, and intelligent fraud prevention in digital banking and e-commerce.

---
