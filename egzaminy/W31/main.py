import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# plt.subplot(2, 3, 2)
#
# sizes = [27.2, 8.8, 28.1, 21.1, 14.9]
# labels = ['A', 'B', 'C', 'D', 'E']
# colors = ['grey', 'lightgrey', 'yellow', 'red', 'lightgreen']
# explode = (0, 0.08, 0, 0, 0)
#
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=25)
#
# plt.title('Tytuł 1')
#
# plt.axis('equal')
#
# plt.subplot(2, 3, 5)
#
# sizes2 = [25.7, 21.2, 13.4, 12.8, 26.8]
# labels2 = ['A', 'B', 'C', 'D', 'E']
# colors2 = ['blue', 'orange', 'brown', 'green', 'red']
# explode2 = (0, 0.1, 0, 0, 0)
#
# plt.pie(sizes2, explode=explode2, labels=labels2, colors=colors2, autopct='%1.1f%%', shadow=True, startangle=20)
#
# plt.title('Tytuł 2')
#
# plt.axis('equal')
#
# plt.tight_layout()
# plt.savefig('zad1.svg', format='svg')
# plt.show()

df = pd.read_excel('ceny31.xlsx')
print(df)

x1 = df[df['Rodzaje towarów i usług']=='jabłka - za 1kg']['Miesiące']
x2 = df[df['Rodzaje towarów i usług']=='cytryny - za 1 kg']['Miesiące']
y1 = df[df['Rodzaje towarów i usług']=='jabłka - za 1kg']['Wartosc']
y2 = df[df['Rodzaje towarów i usług']=='cytryny - za 1 kg']['Wartosc']

maks = max(df[(df['Rodzaje towarów i usług']=='jabłka - za 1kg') |
          (df['Rodzaje towarów i usług']=='cytryny - za 1 kg')]['Wartosc'])

print(maks)
miesiac_maks = df[df['Wartosc']==maks]['Miesiące']
print(miesiac_maks)

plt.plot(x1, y1, ':', linewidth=2, label='Jabłka')
plt.plot(x2, y2, '--', linewidth=1.5, label='Cytryny')
plt.yticks(np.arange(0, 16, 2))
plt.xticks(rotation=45)
plt.tight_layout()
plt.title('Wykres cen wybranych produktów na przestrzeni roku 2016')
plt.legend()
plt.xlabel('Miesiące')
plt.ylabel('Cena za 1kg')
plt.subplots_adjust(bottom=0.23, top=0.9, left=0.1)
plt.annotate('Najwyższy punkt',
             xy=(miesiac_maks, maks),
             xytext=('czerwiec', 10),           # Współrzędne punktu do zaznaczenia                     # Współrzędne początku tekstu
             arrowprops=dict(facecolor='red'),    # Właściwości strzałki (kolor)
             fontsize=12,                         # Rozmiar czcionki
             color='blue',                        # Kolor tekstu
             fontweight='bold')

plt.savefig('zad2.webp', format='webp')
plt.show()