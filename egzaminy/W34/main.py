import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# plt.subplot(2, 3, 2)
# sizes1 = [19.64, 21.43, 36.61, 13.39, 8.93]
# labels1 = ['a', 'b', 'c', 'd', 'e']
# explode1 = (0, 0, 0.2, 0, 0)
# kolory1 = ['brown', 'yellow', 'green', 'beige', 'blue']
#
# plt.pie(sizes1, explode=explode1, colors=kolory1, labels=labels1, autopct='%1.2f%%', shadow=True, startangle=30)
#
# plt.subplot(2, 3, 5)
# sizes2 = [16.2, 19.5, 24.0, 11.0, 29.2]
# labels2 = ['a', 'b', 'c', 'd', 'e']
# explode2 = (0, 0, 0.2, 0, 0.08)
# kolory2 = ['brown', 'yellow', 'green', 'beige', 'blue']
#
# plt.pie(sizes2, explode=explode2, colors=kolory2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=25)
#
# plt.tight_layout()
# plt.savefig('zad1.svg', format='svg')
# plt.show()

# df = pd.read_excel('sprzedaz34.xlsx')
# print(df)
# X = np.arange(3)
#
# data1 = df[df['Produkt']=='Jabłka']['Sprzedaż']
# data2 = df[df['Produkt']=='Gruszki']['Sprzedaż']
# data3 = df[df['Produkt']=='Morele']['Sprzedaż']
# maks = max(df['Sprzedaż'])
# rok_maks = df[df['Sprzedaż']==maks]['Rok']
# print(rok_maks)
#
# plt.bar(X + 0.00, data1, color='b', width=0.25, label="A")
# plt.bar(X + 0.25, data2, color='g', width=0.25, label="B")
# plt.bar(X + 0.50, data3, color='r', width=0.25, label="C")
# labelsbar = np.arange(2015, 2018)
# plt.xticks(X+0.25, labelsbar)
# plt.annotate(' ',
#              xy=(0+0.25, maks),
#              xytext=(0+0.25, 1500),
#              arrowprops=dict(facecolor='red'),
#              fontsize=12,
#              color='blue',
#              fontweight='bold')
# plt.legend()
#
# plt.tight_layout()
# plt.savefig('zad2.webp', format='webp')
# plt.show()

df = pd.read_csv('gastronomia34.csv', header=None, sep=';')
df = df.transpose()

plt.subplot(2, 1, 1)
x1 = df[df[0]=='restauracje'][1]
y1 = df[df[0]=='restauracje'][2].values

liczby = []

for napis in y1:
    napis_bez_spacji = napis.replace(' ', '')  # Usunięcie spacji z napisu
    liczba = int(napis_bez_spacji)  # Zamiana napisu na liczbę całkowitą
    liczby.append(liczba)





plt.plot(x1, liczby, label='Restauracje')

plt.subplot(2, 1, 2)
x2 = df[df[0]=='bary'][1]
y2 = df[df[0]=='bary'][2]

liczby2 = []

for napis in y2:
    napis_bez_spacji = napis.replace(' ', '')  # Usunięcie spacji z napisu
    liczba = int(napis_bez_spacji)  # Zamiana napisu na liczbę całkowitą
    liczby2.append(liczba)

plt.plot(x2, liczby2, label='Bary')




plt.show()