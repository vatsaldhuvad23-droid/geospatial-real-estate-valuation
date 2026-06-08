# Data cleaning and preprocessing
import pandas as pd

df = pd.read_csv("data/kc_house_data.csv")

print(df.head()) 
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.duplicated().sum())
df.to_csv(
    "data/cleaned_housing.csv",
    index=False
) #No missing values
  #No duplicate rows
  #Clean dataset saved