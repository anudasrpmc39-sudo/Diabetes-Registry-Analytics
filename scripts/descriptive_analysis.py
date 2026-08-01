import pandas as pd

# Load dataset
df = pd.read_csv("data/synthetic_diabetes_registry_700000.csv")

# Create outputs folders automatically if they don't exist
import os
os.makedirs("outputs/tables", exist_ok=True)

summary = pd.DataFrame({
    "Indicator": [
        "Total Patients",
        "Average Age",
        "Average BMI",
        "Average HbA1c",
        "Average eGFR",
        "Average Creatinine"
    ],
    "Value": [
        len(df),
        round(df["Age"].mean(), 1),
        round(df["BMI"].mean(), 1),
        round(df["HbA1c_pct"].mean(), 2),
        round(df["eGFR"].mean(), 2),
        round(df["Creatinine_mg_dL"].mean(), 2)
    ]
})

print(summary)

summary.to_csv("outputs/tables/summary_statistics.csv", index=False)

print("\nSummary table saved successfully!")