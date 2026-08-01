import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/synthetic_diabetes_registry_700000.csv")

print("Dataset Loaded Successfully!")
print(df.shape)