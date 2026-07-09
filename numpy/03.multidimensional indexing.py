import numpy as np
arr3 = np.array([
    [
        ['A','B','C'],
        ['D','E','F'],
        ['G','H','I']
    ],
    [
        ['J','K','L'],
        ['M','N','O'],
        ['P','Q','R']
    ],
    [
        ['S','T','U'],
        ['V','W','X'],
        ['Y','Z','']
    ]
    
])
print(arr3[0,0,0]) #A
print(arr3[0,0,1]) #B
print(arr3[0,0,2]) #C
print(arr3[0,1,2]) #F
print(arr3[1,1,1]) #N

print("printing a word from the 3D array")

word = arr3[2,0,1]+arr3[0,2,1]+arr3[0,0,0]+arr3[1,2,2]+arr3[2,0,2]
print(word) 