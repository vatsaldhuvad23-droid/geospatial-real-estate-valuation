# Data cleaning and preprocessing

import pandas as pd

# Load dataset
df = pd.read_csv("data/kc_house_data.csv")

# Display first rows
print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Duplicate rows
print(df.duplicated().sum())

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# Outlier Treatment

Q1 = df["price"].quantile(0.25)

Q3 = df["price"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR

upper = Q3 + 1.5 * IQR

print("Lower Limit:", lower)

print("Upper Limit:", upper)

print("Original Rows:", len(df))

df = df[
    (df["price"] >= lower)
    &
    (df["price"] <= upper)
]

print("Rows After Outlier Removal:", len(df))


df.to_csv(
    "data/outlier_removed.csv",
    index=False
)