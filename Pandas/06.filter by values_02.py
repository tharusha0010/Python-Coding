import pandas as pd
import os
os.system('cls')

calories = {"Day 01": 1750,"Day 02" :2100,"Day 03" :1700}
series = pd.Series(calories)

series.loc["Day 03"] += 500
print(series.loc["Day 02"])