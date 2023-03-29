import math

#ZADANIE 1
# a, b= list(input("Podaj 2 liczby calkowite po spacji:").split(" "))
# a = int(a)
# b = int(b)
#
# #ogarnac try except
#
# wynik = a**2 + a*b + b**2
# plik = open("zadanie1.txt", "w+")
# plik.writelines(str(wynik))
# plik.close

#ZADANIE 2
# def suma(l1, l2):
#     lista = []
#     for i in range(0, len(l1)):
#         lista.append(l1[i] + l2[i])
#     return lista
#
# l1 = [10,15,20]
# l2 = [1,2,3]
# print(suma(l1,l2))

#ZADANIE 3
# plik = open("tekst.txt", "r", encoding='utf8')
# plik.seek(100)
# znaki = plik.read(35)
# print(znaki)
# plik.close
# wynik = 0
# lista = []
# for i in range(0, len(znaki)):
#     if znaki[i].isupper():
#         wynik += 1
#         lista.append(znaki[i])
# if wynik == 0:
#     print("Nie ma duzych znakow")
# else:
#     print(wynik, lista)

#ZADANIE 4
# l1 = [10, 12, 22, 5, 50, 13]
# a = 10
# l2 = [x for x in l1 if x > a]
# print(l2)


#ZADANIE 5
# wynik = (math.e**3 + math.cos(39)**2)**(1/5) + (2/7)**3 + math.pi
# print(round(wynik, 2))