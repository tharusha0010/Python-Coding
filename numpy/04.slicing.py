import numpy as np

arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

#arr2d[start : end : step]
"""
start : කැපීම පටන් ගන්නා දර්ශකය (Index එක) - මෙහි ඇති දත්තය ඇතුළත් වේ.

end : කැපීම අවසන් වන දර්ශකය - මතක තබා ගන්න, මෙම index එකට මෙහා පැත්තෙන් කැපීම නතර වේ (end index එකේ දත්තය අහුවෙන්නේ නැත).

step : පනින්න ඕනේ පියවර ගණන (Default එක 1 වේ).
"""

print(arr2d[0:3])

print("")
print(arr2d[0:4])

print('step')
print(arr2d[0:4:2])

print("print(arr2d[::2])")
print(arr2d[::2])

print("")
print("print(arr2d[::-1])")
print(arr2d[::-1])

print("")
print("print(arr2d[::-2])")
print(arr2d[::-2])

 
