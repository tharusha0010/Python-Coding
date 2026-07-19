import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")

#1.Drop Irrelevant columns
df = df.drop(columns=["Legendary","No"])
print(df.to_string())