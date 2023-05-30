import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import math

#numpy
#z1
# a = np.arange(0, 20*4, 4)

#tworzenie macierzy
# m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     #splaszczanie
# m = m.flatten()

#tworzenie macierzy wartosci ciagu arytmetycznego
# start = 1
# krok = 1
#     #wygeneruj ciag
# ciag = np.arange(start, start + 5*5*krok, krok)
#     #przeksztalc w macierz
# m = ciag.reshape(5, 5) #ew np.reshape(ciag, (5, 5))
# print(m)

#wycinanie macierzy
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# # Wycięcie pierwszego wiersza
# wiersz_1 = matrix[0, :]
# print("Pierwszy wiersz:")
# print(wiersz_1)
# # Output: [1 2 3]
#
# # Wycięcie drugiej kolumny
# kolumna_2 = matrix[:, 1]
# print("Druga kolumna:")
# print(kolumna_2)
# # Output: [2 5 8]
#
# # Wycięcie fragmentu macierzy
# fragment = matrix[1:3, 0:2]
# print("Fragment macierzy:")
# print(fragment)
# # Output:
# # [[4 5]
# #  [7 8]]

#pandas
#z1
# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)

#z2
    #a
# grouped_sum = df.groupby('Rok')['Liczba'].sum()
# wynik = grouped_sum[grouped_sum>1000]
# print(wynik)
    #b
# moje = df[df['Imie'] == 'KAROL']
# print(moje)
    #c
# suma = df['Liczba'].sum()
# print(suma)
    #d
# suma = df[(df['Rok'] > 2000) & (df['Rok'] < 2005)]['Liczba'].sum()
# print(suma)
    #e
# chlopcy = df[df['Plec']=='M']['Liczba'].sum()
# dziewczyny = df[df['Plec']=='K']['Liczba'].sum()
# print(chlopcy)
# print(dziewczyny)
    #f i g
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
#
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# # print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])

#z3
# df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
# print(df)
    #a
# unikalne = df['Sprzedawca'].unique()
# print(unikalne)
    #b
# wynik = df.sort_values('Utarg', ascending=False).head(5)
# print(wynik)
    #c
# grupa = df.groupby('Sprzedawca')
# wynik = grupa['idZamowienia'].count()
# print(wynik) #lub df.groupby('Sprzedawca').size()
    #d
# grupa = df.groupby('Kraj')
# wynik = grupa['Utarg'].sum()
# print(wynik) # lub df.groupby('Kraj').agg({'Utarg': ['sum']})
    #e
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# df['Rok'] = df['Data zamowienia'].dt.year
# grupa = df[(df['Rok'] == 2005) & (df['Kraj'] == 'Polska')]
# wynik = grupa['Utarg'].sum()
# print(wynik)
    #f
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# df['Rok'] = df['Data zamowienia'].dt.year
# grupa = df[(df['Rok'] == 2004)]
# wynik = grupa['Utarg'].sum()
# ilosc = grupa['Utarg'].count()
# print(wynik/ilosc) #lub df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']})
    #g
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# grupa04 = df[df['Data zamowienia'].dt.year == 2004]
# grupa04.to_csv("zamowienia_2004.csv", index=False)

#wykresyPandas

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# zad1
# roczniki = df['Rok'].unique()
# grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
# wykres = grupa.plot()
# wykres.set_ylabel('Liczba urodzonych dzieci')
# wykres.set_xticks(roczniki)
# wykres.tick_params(axis='x', labelrotation=40)
# wykres.legend()
# plt.subplots_adjust(left=0.15, right=0.9, bottom=0.15, top=0.9)
# plt.title("Liczba urodzonych dzieci dla każdego roku")
# plt.show()
# #zad2
# grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.bar(ylabel='Liczba urodzeń')
# wykres.legend()
# plt.xticks(rotation=0)
# plt.title("Liczba urodzonych chłopców i dziewczynek")
# plt.show()
#zad3
# grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
# plt.legend()
# plt.show()
#zad4
# df = pd.read_csv('zamowienia.csv', delimiter=';')
# policzone = df.groupby('Sprzedawca').size()
# policzone.plot.bar()
# plt.ylabel("liczba zamówień")
# plt.subplots_adjust(left=0.1, right=0.9, bottom=0.2, top=0.9)
# plt.title('Ilość zamówień sprzedawców')
# plt.show()

#matplotlib

#z1
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, len(x), 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()

#z2
# x = np.arange(1, 21, 1)
# plt.plot(x-1, 1/x, 'g^:', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, len(x), 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()

#z3
# x = np.arange(0, 30.1, 0.1)
# y1 = np.sin(x)
# y2 = np.cos(x)
# plt.plot(x, y1, 'r', label='Sin(x)')
# plt.plot(x, y2, 'g', label='Cos(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.legend(bbox_to_anchor=(0.2, 1.15))
# plt.show()

#z4
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# colors = np.random.randint(0, 50, len(df.index))
# scale = np.abs(df['sepal length'] - df['sepal width'])
# plt.scatter(data=df, x='sepal length', y='sepal width', c=colors, s=scale)
# plt.title('Wykres punktowy')
# plt.xlabel('Sepal length')
# plt.ylabel('Sepal width')
# plt.legend()
# plt.show()

#z5
# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)
#     #a
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
#     #b
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# ch = df[df['Plec']=='M'].groupby('Rok')['Liczba'].sum()
# dz = df[df['Plec']=='K'].groupby('Rok')['Liczba'].sum()
# plt.plot(x, dz, label='Kobiety')
# plt.plot(x, ch, label='Mezczyzni')
# plt.xlabel('Rok')
#     #c
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# suma = df.groupby('Rok')['Liczba'].sum()
# plt.bar(x, suma)
# plt.xlabel('Rok')
#
# plt.subplots_adjust(wspace=0.85)
# plt.tight_layout()
# plt.show()

#Proba
#1
# x = np.arange(1, 21, 1)
# y = 2*x + 5
# plt.plot(x, y, label='f(x)')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.legend()
# plt.tight_layout()
# plt.show()

#2
# x = np.arange(0, 2, 0.02)
# y1 = np.sin(x * np.pi * 2)
# y2 = np.cos(x * np.pi * 2)
#
# plt.subplot(3, 2, 1)
# plt.plot(x, y1)
# plt.title('wykres sin(x)')
# plt.axis([0, 2, -1, 1])
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#
# plt.subplot(3, 2, 4)
# plt.plot(x, y2, 'r')
# plt.title('wykres cos(x)')
# plt.axis([0, 2, -1, 1])
# plt.xlabel('x')
# plt.ylabel('cos(x)')
#
# plt.subplot(3, 2, 5)
# plt.plot(x, y2, 'r')
# plt.title('wykres cos(x)')
# plt.axis([0, 2, -1, 1])
# plt.xlabel('x')
# plt.ylabel('cos(x)')
#
# plt.show()

#3
# df = pd.read_excel('imiona.xlsx', header=0)
# print(df)
# suma = df.groupby('Rok').sum()
# suma.plot.bar()
# plt.xticks(rotation=45)
# plt.subplots_adjust(left=0.2, right=0.8, bottom=0.2, top=0.9)
# plt.title('Ilość urodzonych dzieci w kazdym roku')
#
# plt.show()



