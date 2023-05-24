import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from PIL import Image

# plt.plot([1, 3, -5, 7])
# plt.show()

# x = np.array([1, 2, 3, 4])
# y = x**2
#
# plt.plot(x, y, 'ro-')
# plt.axis([0, 6, 0, 20])
# plt.show()
# plt.plot(x, y, 'r')
# plt.plot(x, y, 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

# x = np.arange(0, 5, 0.2)
# plt.plot(x, x, 'r--', label='liniowa')
# plt.plot(x, x**2, 'bo', label='kwadratowa')
# plt.plot(x, x**3, 'g^', label='szescienna')
# plt.legend(loc='center')
# plt.show()

# wykres sinusa na przedziale x<0,10> wartosci zmieniaja sie co 0.1

# x = np.arange(0, 10, 0.1)
# y = [math.sin(i) for i in x]
# plt.plot(x, y)
# plt.xlabel('os x')
# plt.ylabel('os y')
# plt.legend(labels=['sin(x)'])
# plt.title('wykres liniowy funkcji sinus')
# plt.show()

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)
# }
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# plt.scatter('a', 'b', c='c', s='d', data=data, cmap='plasma')
# plt.xlabel('klucz a')
# plt.ylabel('klucz b')
# plt.show()

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(x1 * np.pi * 2)
# y2 = np.cos(x2 * np.pi * 2)
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1)
# plt.title('wykres sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2)
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

#To samo co wyzej ale siatka 4x1 a nie 2x1
# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(x1 * np.pi * 2)
# y2 = np.cos(x2 * np.pi * 2)
# plt.subplot(4, 1, 1)
# plt.plot(x1, y1)
# plt.title('wykres sin(x)')
#
# plt.subplot(4, 1, 4)
# plt.plot(x2, y2)
# plt.title('wykres cos(x)')
# plt.show()

# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1)
# axs[0, 0].set_title('Sinus')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('y')
#
# axs[1, 1].plot(x2, y2)
# axs[1, 1].set_title('Cosinus')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('y')
#
# axs[2, 0].plot(x1, y1, 'r')
# axs[2, 0].set_title('Sinus')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('y')
#
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
#
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
#
# plt.show()
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
#
# df = pd.DataFrame(data)
# print(df)
# # grupa = df.groupby('Kontynent')
# # etykiety = list(grupa.groups.keys())
# # wartosci = list(grupa.agg('Populacja').sum())
# #
# # plt.bar(etykiety, wartosci, color=['yellow', 'red', 'green'])
# # plt.xlabel('Kontynenty')
# # plt.ylabel('Populacja')
# # plt.show()
#
# grupa = df.groupby('Kontynent').agg({'Populacja': ['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel='Kontynenty', ylabel='Populacja',
#            legend=True, rot=0, title='Populacja na kontynentach')
# plt.savefig('wykres.png')
# plt.show()

# ts = pd.Series(np.random.randn((1000)))
# ts = ts.cumsum()
# ts.plot()
# plt.show()

df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)
grupa = df.groupby('Imię i nazwisko').agg('Wartość zamówienia')
grupa.plot(kind='pie', subplot=True, autopct='%.2f%%', fontsize=20, figsize=(6, 6), colors=['red', 'green'])
plt.legend(loc='lower right')
plt.title('Procent zamowienia dla sprzedawcy')
plt.show()