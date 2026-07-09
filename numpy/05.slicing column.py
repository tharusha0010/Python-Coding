
import numpy as np

arr2d = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

print("column 01")
print(arr2d[:,1])

print("column 02")
print(arr2d[:,2])

print("last column ")
print(arr2d[:,-1])

print("2nd last column ")
print(arr2d[:,-2])

print("first 3 columns ")
print(arr2d[:,0:3])

print("skip 1st column ")
print(arr2d[:,1:4])

print("every 2nd column")
print(arr2d[:,::2])

print("")
print(arr2d[:,1::2])

print("print(arr2d[0:2,0:2])")
print(arr2d[0:2,0:2])

