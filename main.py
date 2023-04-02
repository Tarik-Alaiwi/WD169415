import math
 #ZADANIE 1
# plik = open("tekst.txt", "r", encoding='utf8')
# plik.seek(71)
# znaki =  plik.read(40)
# print(znaki)
# plik.close()
# wynik = 0
# lista = []
# for i in range(0, len(znaki)):
#     if znaki[i] == 'A':
#         wynik += 1
#         lista.append(znaki[i])
# if wynik == 0:
#     print("znaku 'A' nie ma we fragmencie")
# else:
#     print(wynik)

#ZADANIE 2
# a = [1.0,2,10.15,15,626.2,12,3]
# b = [x for x in a if type(x)==float]
# print(a)
# print(b)

#ZADANIE 3
# def suma(list1):
#     list2 = []
#     for i in range(0, len(list1)):
#        list2.append( list1[0]+list1[i])
#     return list1+list2
#
# list1 = [1,3,5,10]
# print(suma(list1))

#ZADANIE 4
# wynik = (math.sin(56))**2+(((4**2)/25)+math.log(85, 3))**(1/4)
# print(wynik)

#ZADANIE 5
# n = input("podaj liczbe calkowita n: ")
# try:
#     n = int(n)
# except ValueError:
#     print("podaj liczbe calkowita!")
#
#
# wynik = 0
#
# for i in range(1, n+1):
#     wynik += i
#
# plik = open("zadanie5.txt", "w+")
# plik.writelines(str(wynik))
# plik.close()
