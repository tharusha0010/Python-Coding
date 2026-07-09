import os
import numpy as np
os.system('cls')
print("comparison operations")

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Element-wise equality:", arr1 == arr2)
print("Element-wise not equal:", arr1 != arr2)
print("Element-wise less than:", arr1 < arr2)
print("Element-wise greater than:", arr1 > arr2)
print("Element-wise less than or equal:", arr1 <= arr2)
print("Element-wise greater than or equal:", arr1 >= arr2)

print(" ")
print("example 2")
scores = np.array([91,55,100,73,82,64])
print(scores == 100)
print(scores >= 60 )
scores[scores >= 60] = 1
print("scores greater than or equal to 60 =1:", scores)

