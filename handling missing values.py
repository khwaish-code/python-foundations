import pandas as pd
import numpy as np

data = {
    "Name": ["Khwaish", "Mishee", "Harshit", "Riya", "Palomi"],
    "Marks": [85, np.nan, 90, np.nan, 88],
    "Age": [20, 21, np.nan, 22, 23]
}

df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

print("\nMissing Values in Dataset:\n")
print(df.isnull())

print("\nTotal Missing Values in Each Column:\n")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nDataset After Handling Missing Values:\n")
print(df)