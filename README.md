#  LLM-Enhanced E-Commerce Fraud Detection

##  Project Overview

This project is an **LLM-Enhanced E-Commerce Fraud Detection System** that combines a traditional machine learning model (**XGBoost**) with a **Large Language Model (LLaMA via Hugging Face)** to detect fraudulent transactions and generate human‑readable explanations. A simple **Streamlit UI** is used to interact with the model and display predictions.

---

##  Project Files

```
LLM-Enhanced-E-Commerce-Fraud-Detection/
│
├── Fraud_Data.csv          # Dataset used for fraud prediction
├── xgb_classifier.pkl     # Trained XGBoost model file
├── model.py               # Loads model and performs fraud prediction
├── app.py                 # Streamlit app (UI + LLM integration + prediction)
└── README.md              # Project documentation
```

---

##  Technologies Used

* **Python** – Core programming language
* **XGBoost** – Machine learning classifier for fraud detection
* **Streamlit** – Web interface for prediction
* **Hugging Face Transformers (LLaMA)** – Text generation and explanation
* **Pandas, NumPy, Scikit‑learn** – Data preprocessing and evaluation

---

##  Model Description

* The fraud detection model is trained using **XGBoost** on transaction data from `Fraud_Data.csv`.
* The trained model is saved as `xgb_classifier.pkl`.
* `model.py` loads this trained model and performs prediction on new transactions.

---

##  LLM Integration

* The **LLaMA Hugging Face transformer model is integrated directly inside `app.py`**.
* After predicting fraud / non‑fraud using the XGBoost model, the application:

  * Sends transaction context to the LLaMA model
  * Generates natural‑language explanations and risk descriptions

This allows the system to provide **explainable AI outputs** along with fraud predictions.

---

##  Streamlit User Interface

* Implemented in `app.py`
* Features:

  * Input transaction details
  * Predict fraud using trained XGBoost model
  * Display AI‑generated explanation using LLaMA

---

## How to Run the Project

###  Install Required Libraries

```bash
pip install streamlit xgboost pandas numpy scikit-learn transformers torch
```

---

###  Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser and allow you to test fraud predictions interactively.

---

##  Input & Output

**Input:** Transaction details from user or dataset
**Output:**

* Fraud Prediction: `Fraud` / `Not Fraud`
* Prediction Probability
* LLaMA Generated Explanation Text

---

##  Use Case

This system helps e‑commerce platforms:

* Detect fraudulent transactions in real time
* Provide explainable AI decisions
* Improve customer trust and transaction security

---

##  Author

**Chandana T S**
Computer Science Student | Machine Learning & AI Enthusiast

---

## Note

This project demonstrates the integration of **traditional ML models with LLMs** to build an explainable and intelligent fraud detection system.
