import pandas as pd
import os
os.system('cls')

data = [100,102,104]
series = pd.Series(data, index=["number1","number2","number3"])
print(series)