import numpy as np

# #ZADANIE 1
# a = np.array([0, 1, 2])
# b = np.array([0, 1, 2])
#
# c = np.dot(a, b)
# print(c)

#ZADANIE 2
a = np.array([[0, 1, 2], [2, 5, 6], [8, 4, 8]])
b = np.array([[0, 1, 2, 5], [2, 5, 6, 3], [8, 4, 8, 4], [3, 3, 3, 3]])

wynik = min(a[0])

for x in a:
    if wynik > min(x):
        wynik = x
print(wynik)



