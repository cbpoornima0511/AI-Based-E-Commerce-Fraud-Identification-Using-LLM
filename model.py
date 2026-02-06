import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

# =========================
# 1. Load Dataset
# =========================
df = pd.read_csv("Fraud_Data.csv")

# =========================
# 2. Feature Engineering
# =========================
df["signup_time"] = pd.to_datetime(df["signup_time"])
df["purchase_time"] = pd.to_datetime(df["purchase_time"])

# Time difference between signup and purchase (seconds)
df["time_diff"] = (
    df["purchase_time"] - df["signup_time"]
).dt.total_seconds()

# Encode browser
browser_encoder = LabelEncoder()
df["browser_encoded"] = browser_encoder.fit_transform(df["browser"])

# Final feature set (simple & clean)
X = df[[
    "purchase_value",
    "time_diff",
    "browser_encoded"
]]

y = df["class"]

# Handle missing values
X = X.fillna(0)

# =========================
# 3. Train-Test Split
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# =========================
# 4. Train XGBoost Model
# =========================
model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=(y_train == 0).sum() / (y_train == 1).sum(),
    objective="binary:logistic",
    eval_metric="auc",
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# 5. Evaluation
# =========================
y_pred_prob = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred_prob)
print(f"XGBoost ROC-AUC: {auc:.4f}")

# =========================
# 6. Save Model & Encoder
# =========================
with open("xgb_classifier.pkl", "wb") as f:
    pickle.dump(model, f)

with open("browser_encoder.pkl", "wb") as f:
    pickle.dump(browser_encoder, f)

print("✅ XGBoost model saved using pickle")
