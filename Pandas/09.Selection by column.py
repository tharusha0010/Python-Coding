import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")

#SELECTION BY COLUMN

#print(df["Name"].to_string())
#print(df["Height"].to_string())

print(df[["Name","Height","Weight"]].to_string())