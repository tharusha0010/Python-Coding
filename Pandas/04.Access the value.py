import os
import pandas as pd
os.system('cls')

data = [100,102,103]
series = pd.Series(data , index=["num1","num2","num3"])
series.loc["num1"] = 200
print("new value os num1 is:",series.loc["num1"])
print(series)

print("")
print("access location by integer value")
print(series.iloc[2])