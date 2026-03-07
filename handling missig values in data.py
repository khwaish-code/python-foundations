import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Riya", "John", "Sara", "Mike"],
    "Marks": [85, np.nan, 90, np.nan, 88],
    "Age": [20, 21, np.nan, 22, 23]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values in Dataset:")
print(df.isnull())

print("\nTotal Missing Values:")
print(df.isnull().sum())

df["Marks"].fillna(df["Marks"].mean(), inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)

print("\nData After Handling Missing Values:")
print(df)