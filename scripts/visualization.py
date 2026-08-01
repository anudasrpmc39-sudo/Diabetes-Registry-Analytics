import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/synthetic_diabetes_registry_700000.csv")

print("Creating chart...")

plt.figure(figsize=(8,5))

plt.hist(df["Age"], bins=20, edgecolor="black")

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")

plt.tight_layout()

plt.savefig("Age_Distribution.png")

print("Chart saved successfully!")

plt.show()

print("Finished!")