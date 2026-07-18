import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv" , index_col="Name")
pokemon = input("Enter a pokemon name:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")    