import random
import math
#ZADANIE 1:

# A = [1-x for x in range(1, 11)]
# print(A)
# B = [4**x for x in range(0, 8)]
# print(B)
# C = [x for x in B if x % 2 == 0]
# print(C)

#ZADANIE 2:

# lista1 = []
# for i in range(1, 10):
#     lista1.append(random.randint(0,100))
# print(lista1)
# A = [x for x in lista1 if x % 2 == 0]
# print(A)

#ZADANIE 3:

# zakupy = {"mleko": "ml", "mieso": "kg", "papier": "sztuki" }
# print(zakupy)
# nzakupy = {x for x in zakupy if zakupy[x] == "sztuki"}
# print(nzakupy)

#ZADANIE 4:

# def czy_prostokatny(kat1, kat2, kat3):
#     if kat1 == 90 or kat2 == 90 or kat3 == 90:
#         print("jest prostokatny")
#     else:
#         print("nie jest prostokatny")
#
# print("podaj 3 katy: ")
# kat1 = int(input())
# kat2 = int(input())
# kat3 = int(input())
#
# print(czy_prostokatny(kat1, kat2, kat3))

#ZADANIE 5:

# def pole_trapezu(a=1, b=1, h=1):
#     return ((a+b)*h)/2
#
# print("podaj wymiary trapezu")
# a = int(input())
# b = int(input())
# h = int(input())
# print(pole_trapezu(a, b, h))

#ZADANIE 6:

# def iloczyn(a1 = 1, b = 4, ile = 10):
#     wynik = 1
#     wynik *= b**(ile-1)
#     return wynik
# print(iloczyn(1, 4, 2))

#ZADANIE 7:

# def iloczyn(a1 = 1, b = 4, ile = 10):
#     wynik = 1
#     wynik *= b**(ile-1)
#     return wynik
# print(iloczyn(1, 4, 2))

#ZADANIE 8:

# def ilosc_wartosc(**zakupy):
#     koszt = sum(zakupy.values())
#     ilosc = len(zakupy)
#     return koszt, ilosc
#
# zakupy = {"jablka": 5, "banany": 5, "kiwi": 10}
# koszt, ilosc = ilosc_wartosc(**zakupy)
# print(f"{ilosc} elementow kosztuje {koszt}zl")

#ZADANIE 9:

# x = int(input("Podaj liczbe: "))
#
# try:
#     sqrt = math.sqrt(x)
# except ValueError:
#     print("Podaj ujemna liczbe")
#     exit()
#
# print(sqrt)
#
# print(x)