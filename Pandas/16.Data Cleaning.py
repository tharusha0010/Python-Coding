import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")

#1.Drop Irrelevant columns
#df = df.drop(columns=["Legendary","No"])
#print(df)

#2. Handle missing data(na=not available)
#df = df.dropna(subset=["Type2"])
#print(df.to_string())

#df = df.fillna({"Type2" :"None"})
#print(df.to_string())

#3. Fix inconsistent values
#df["Type1"] = df["Type1"].replace({"Grass":"GRASS"})
#print(df.to_string())


#4.Standardize text
#df["Name"]= df["Name"].str.lower()
#print(df.to_string())

#5.Fix data types
#df["Legendary"] = df["Legendary"].astype(bool)
#print(df.to_string())

#6.Remove duplicates values
#df = df.drop_duplicates()
#print(df.to_string())

