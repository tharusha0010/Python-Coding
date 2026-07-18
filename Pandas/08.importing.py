import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")
print(df.to_string())