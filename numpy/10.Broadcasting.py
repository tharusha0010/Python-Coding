import os
import numpy as np
os.system('cls')

"""
💡 Broadcasting නීතියේ සාරාංශය
ඉලක්කම් සමාන නම්: NumPy ට ප්‍රශ්නයක් නැහැ, දෙන්නගේම පළල හෝ උස සමාන නිසා කෙළින්ම එකතු කරනවා.
එකක් 1 නම්: NumPy ට ප්‍රශ්නයක් නැහැ, ඒ 1 තියෙන පැත්ත අනිත් ලොකු ඉලක්කමේ ගාණට එනකම් ඇදලා
(Virtually Copy කරලා) සමාන කරගන්නවා.
ඉලක්කම් දෙක වෙනස් වෙලා, එකක්වත් 1 නොවෙයි නම් (උදා: 3 සහ 2): අන්න එතනදී NumPy ට ඇදලා ලොකු කරන්නත් බැහැ,
සමානත් නැහැ. ඒ නිසා වැඩේ වරදිනවා (Error).
"""

A = np.array([
    [1,2,3,4]
])

B = np.array([
    [1],
    [2],
    [3],
    [4]
])

print("A shape:", A.shape)
print("B shape:", B.shape)
print(A * B) 

print(" ")

C =np.array([
    [1,2,3,4,5,6,7,8,9,10]
])

D = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

print("C shape:", C.shape)
print("D shape:", D.shape)
print(C+D)