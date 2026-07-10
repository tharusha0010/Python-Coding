import os
import numpy as np
os.system('cls')

arr1 = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print("sum of arr1:", np.sum(arr1))
print("mean of arr1:", np.mean(arr1))
print("standard deviation of arr1:", np.std(arr1))
print("variance of arr1:", np.var(arr1))
print("minimum value:",np.min(arr1))
print("maximum value:",np.max(arr1))
print("position of min:",np.argmin(arr1))
print("position of max:",np.argmax(arr1))
