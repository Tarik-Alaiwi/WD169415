import numpy as np

# #ZADANIE 1
# a = np.arange(0,81,4)
# print(a)
#
# #ZADANIE 2
# a = np.arange(10, dtype='float')
# print(a)
# print(a.dtype)
# b= a.astype('int32')
# print(b)
# print(b.dtype)

# #ZADANIE 3
# def f(n):
#     tab = np.array([2**i for i in range(n**2)])
#     return tab.reshape((n,n))
# n = 5
# print(f(n))

# # ZADANIE 4
# def f(n,m):
#     wynik = np.logspace(1,m, num=m, base=n)
#     return wynik
# n = 2
# m = 4
# print(f(n,m))

# # ZADANIE 5
# def diagonalna(n):
#     a = np.arange(n,-1,-1)
#     diag = np.diag(a,2)
#     return diag
#
# print(diagonalna(4))

# # ZADANIE 6
# malina = np.array(list("malina"))
# mrowka = np.array(list("mrowka"))
#
# wykreslanka = np.zeros((6,6), dtype='str')
#
# print(wykreslanka)

# # ZADANIE 7
# def macierz(n):
#     mac = np.zeros((n,n), dtype='int32')
#     mac += np.diag([2 for _ in range(n)])
#     for i in range(1,n):
#         mac += np.diag([2+(2*i) for _ in range(n-i)], k =i)
#         mac += np.diag([2+(2*i) for _ in range(n-i)], k =-i)
#     print(mac)
#
# macierz(3)

#ZADANIE 8
