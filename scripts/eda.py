import pandas as pd

# Load dataset
df = pd.read_csv("data/synthetic_diabetes_registry_700000.csv")

print("="*60)
print("Dataset Shape")
print(df.shape)

print("\n" + "="*60)
print("Dataset Information")
print(df.info())

print("\n" + "="*60)
print("Missing Values")
print(df.isnull().sum())

print("\n" + "="*60)
print("Duplicate Rows")
print(df.duplicated().sum())

print("\n" + "="*60)
print("First 5 Rows")
print(df.head())