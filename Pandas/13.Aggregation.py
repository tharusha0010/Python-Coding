import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")
print(df.mean(numeric_only=True))

print("Sum")
print(df.sum(numeric_only=True))

print("Minimum")
print(df.min(numeric_only=True))

print(df.max(numeric_only=True))

print(df.count())