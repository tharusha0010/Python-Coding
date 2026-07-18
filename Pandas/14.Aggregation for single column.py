import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")

# Whole dataframe aggregation operations
"""
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())

"""

#Single column
print(f"Mean of Heights : {df["Height"].mean()}")
print(f"Sum of all Heights :{df["Height"].sum()}")
print(f"minimum  Height :{df["Height"].min()}")
print(f"maximum  Height :{df["Height"].max()}")