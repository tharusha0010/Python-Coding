import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv", index_col = "Name")
#SELECTION BY ROWS
print(df.loc["Charizard":"Blastoise",["Height","Weight"]])


print("")
print("First 10 rows")
print(df.iloc[0:11])