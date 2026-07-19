import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")

#2. Handle missing data(na=not available)
df = df.dropna(subset=["Type2"])
print(df.to_string())
