import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

#z1
# x = np.arange(0, 31, 0.1)
# y = [math.sin(i) for i in x]
# y1 = [math.cos(i) for i in x]
#
# sns.set(rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=x, y=y, label='y = sin(x)', color='red', linestyle=':')
# sns.lineplot(x=x, y=y1, label='y = cos(x)', color='blue')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres sin(x) i cos(x)')
# plt.legend(bbox_to_anchor=(1.01, 1.1))
# plt.show()

#z2.1
# df = pd.read_excel('imiona.xlsx')
#
# sns.set()
# chlopcy = df[df['Plec'] == 'M'].shape[0]
# dziewczynki = df[df['Plec'] == 'K'].shape[0]
#
# plt.figure(figsize=(8, 6))
#
# sns.barplot(x=['Chłopcy', 'Dziewczynki'], y=[chlopcy, dziewczynki])
# plt.title('Ilość narodzonych chlopcow i dziewczynek')
# plt.xlabel('Płeć')
# plt.ylabel('Ilość narodzin')
#
# plt.show()

#z2.2
#---

#z3
# df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=".")
#
# ilosc = df.groupby('Sprzedawca').size()
#
# sns.set()
# plt.figure(figsize=(10, 6))
# sns.barplot(x=ilosc.index, y=ilosc.values)
#
# plt.title('Ilość zamówień dla każdego sprzedawcy')
# plt.xlabel('Sprzedawca', labelpad=10)
# plt.ylabel('Ilość zamówień')
# plt.xticks(rotation=0)
#
# plt.show()

#z4
# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
#
# plt.figure(figsize=(10, 6))
#
# sns.scatterplot(data=df, x='petal length', y='petal width', hue='class')
# plt.title('Wykres punktowy dla petal length i petal width')
# plt.xlabel('Petal Length')
# plt.ylabel('Petal Width')
# plt.legend()
#
# plt.show()








