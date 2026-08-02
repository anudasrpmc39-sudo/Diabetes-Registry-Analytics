# ======================================================
# Diabetes High-Risk Prediction Model
# Clean Production Version
# ======================================================

import joblib
import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split

# ======================================================
# Paths
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "synthetic_diabetes_registry_700000.csv"
MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(exist_ok=True)

print("Loading dataset...")
df = pd.read_csv(DATA_PATH)

# ======================================================
# Features & Target
# ======================================================

features = [
    "Age",
    "BMI",
    "Duration_Years",
    "FBS_mmol_L",
    "RBS_mmol_L",
    "2HBS_mmol_L",
    "HbA1c_pct",
    "Creatinine_mg_dL",
    "eGFR",
    "LDL_mg_dL",
]

X = df[features]

print("\nHigh_Risk distribution:")
print(df["High_Risk"].value_counts(dropna=False))

# Handle either Yes/No or 0/1
# ======================================================
# Target Variable
# ======================================================
y = df["High_Risk"].map({
    "Yes": 1,
    "No": 0
}).astype(int)

# Convert High_Risk safely
if set(df["High_Risk"].dropna().unique()) == {"Yes", "No"}:
    y = df["High_Risk"].map({
        "Yes": 1,
        "No": 0
    }).astype(int)
else:
    y = pd.to_numeric(df["High_Risk"])
# ======================================================
# Split
# ======================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y,
)

# ======================================================
# Train
# ======================================================

print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
)

model.fit(X_train, y_train)

print("Training complete.")

# ======================================================
# Evaluate
# ======================================================

pred = model.predict(X_test)
prob = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)
auc = roc_auc_score(y_test, prob)

print("\n==============================")
print("MODEL PERFORMANCE")
print("==============================")
print(f"Accuracy : {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall   : {recall:.3f}")
print(f"F1 Score : {f1:.3f}")
print(f"ROC AUC  : {auc:.3f}")
print("\nClassification Report")
print(classification_report(y_test, pred))
print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred))

# ======================================================
# Save
# ======================================================

joblib.dump(model, MODELS_DIR / "diabetes_random_forest.pkl")

metrics = {
    "accuracy": accuracy,
    "precision": precision,
    "recall": recall,
    "f1": f1,
    "auc": auc,
    "confusion_matrix": confusion_matrix(y_test, pred),
    "feature_importance": model.feature_importances_,
    "features": features,
}

joblib.dump(metrics, MODELS_DIR / "model_metrics.pkl")
joblib.dump(features, MODELS_DIR / "feature_names.pkl")

print("\nSaved:")
print(" - diabetes_random_forest.pkl")
print(" - model_metrics.pkl")
print(" - feature_names.pkl")