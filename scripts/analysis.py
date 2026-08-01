import pandas as pd

# Load the dataset
df = pd.read_csv("data/synthetic_diabetes_registry_700000.csv")

# Show the first 5 rows
print(df.head())

# Display information about the dataset
print("\nDataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())