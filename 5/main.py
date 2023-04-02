import math


# slownik = {'mleko': 'sztuki', 'ziemiaki': 'kg', 'jogurt': 'sztuki'}
# lista = [key for key in slownik.keys() if slownik[key] == 'sztuki']
# print(lista)

# def trojkat_prostokatny(a, b, c):
#     if a**2 + b**2 == c**2:
#         return 'trójtkąt prostokątny'
#     else:
#         return 'trójkąt nie jest prostokątny'
# print(trojkat_prostokatny(3, 4, 5))

# def pole_trapezu(a=6,b=3,h=5):
#     return (a+b)*h/2
# print(pole_trapezu())

# def iloczyn(a=1, b=4, ile=10):
#     licznik = 0
#     while licznik != ile:
#         a *= b
#         licznik += 1
#     return a
# print(iloczyn())
# #
# #
# def iloczyn2(*liczby):
#     if len(liczby) == 3:
#         licznik = 0
#         wynik = liczby[0]
#         while licznik != liczby[2]:
#             wynik *= liczby[1]
#             licznik += 1
#         return wynik
#     else:
#         return 'zła ilość liczb wejściowych'
#
# print(iloczyn2(1,4,10))
#
# def iloczyn2(*liczby, b):
#     if len(liczby) == 0:
#         return 0
#     else:
#         iloczyn_liczb = liczby[0] * b
#         licznik = 1
#         while licznik != len(liczby):
#             iloczyn_liczb *= b
#             licznik += 1
#         return iloczyn_liczb
# print(iloczyn2(1,2,3,4,5,6,7,8,9,10,b=4))

# def lista_zakupow(** rzeczy):
#     koszt_zakupow = 0
#     for koszt in rzeczy:
#         koszt_zakupow += rzeczy[koszt]
#     return len(rzeczy), round(koszt_zakupow, 2)
# print(lista_zakupow(mleko=2.78, czekolada=5.40, kawa=22.99))

# a = input('podaj liczbę: ')
# try:
#     a = float(a)
#     pierwiastek = math.sqrt(a)
#     print(pierwiastek)
# except ValueError:
#     if type(a) != float:
#         print('nie wczytano liczby')
#     elif a < 0:
#         print('liczba a nie może być mniejsza od 0')


a = [x * 2 for x in range(0, 31)]

# r - odczyt
# w - zapis
# a - dopis
#
# r+ - odczyt i zapis - plik musi istniec
# w+ - zapis i zapis plik - zostanie stworzony jesli nie istnieje
# a+ - dopis i zapis - zostanie stworzony jesli nie istnieje


# plik = open('zad1.txt', 'w+')
# for b in a:
#     plik.write(str(b))
#     # plik.write('\n')
# plik.seek(0)
# zawartosc = plik.readlines()
# plik.close()
# print(zawartosc)


with open('zad3.txt', 'w') as plik:
    for b in a:
        plik.write(str(b))
        plik.write('\n')
with open('zad3.txt', 'r') as plik:
    for a in plik:
        print(a, end='')
