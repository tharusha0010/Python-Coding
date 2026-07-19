import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")
group = df.groupby("Type1")
#print(group["Height"].mean())
print(group["Height"].sum())