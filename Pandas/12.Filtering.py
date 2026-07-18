import os
import pandas as pd
os.system('cls')

df = pd.read_csv("pandas/data.csv")

#tall_pokemon = df[df["Height"] >= 2]
#print(tall_pokemon)

heavy_pokemon = df[df["Weight"] >100]
print(heavy_pokemon) 

print("")
print("water pokemon")
water_pokemon = df[(df["Type1"] == "Water") |
                   (df["Type2"] == "Water")  ]
print(water_pokemon)