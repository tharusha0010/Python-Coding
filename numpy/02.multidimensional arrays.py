import numpy as np
 
 #2D array
 
arr2d = np.array([[1,2,3],
                  [4,5,6]])
print(arr2d)
print(arr2d.ndim) #Number of dimensions
print(arr2d.shape) #Rows, Columns

#3D array

arr3d = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    
    [
        [7,8,9],
        [10,11,12,]
    ]
])
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)

"""
මෙන්න මේ (2, 2, 3) කියන Shape එක ML වලදී කියවන්නේ මේ විදිහටයි:

පළමු ඉලක්කම (2): තට්ටු හෝ Matrices ගණන (Number of Blocks / Channels).

දෙවැනි ඉලක්කම (2): හැම තට්ටුවකම තියෙන පේළි ගණන (Rows).

තුන්වැනි ඉලක්කම (3): හැම පේළියකම තියෙන තීරු ගණන (Columns).
"""

