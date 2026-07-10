import os
import numpy as np
os.system('cls')

ages = np.array([
    [21,17,19,20,16,30,18,65],
    [39,22,15,99,18,19,20,21]
])

teenagers = ages[ages < 18]
print(teenagers)


adults = ages[(ages >= 18)&(ages < 65)]
print("adults:",adults)

adults2 = ages[(ages < 18) | (ages >= 65)]
print("adults2:",adults2)



