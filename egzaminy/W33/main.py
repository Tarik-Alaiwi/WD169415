import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# data = [[-10, -26, -7, -38],
#         [-13, -20, -15, -7],
#         [-17, -28, -16, -15]]
# Y = np.arange(4)
#
# plt.barh(Y + 0.00, data[0], color='yellow', height=0.25, label="A")
# plt.barh(Y + 0.25, data[1], color='orange', height=0.25, label="B")
# plt.barh(Y + 0.50, data[2], color='blue', height=0.25, label="C")
# labelsbar = ['PL', 'DE', 'FR', 'SK']
# plt.yticks(Y + 0.25, labelsbar)
# plt.grid()
# plt.title('Wykres')
# plt.xlabel('Podpis osi 2', c='g')
# plt.ylabel('Podpis osi 1', c='r')
# plt.legend(loc='upper center')
#
# plt.savefig('zad1.tiff', format='tiff')
# plt.show()

# df = pd.read_excel('ceny33.xlsx')
#
# new_df = df[df['Rodzaje towarów i usług']=='jabłka - za 1kg']
# print(new_df)
# ceny = new_df['Wartosc']
# mies = new_df['Miesiące']
# plt.scatter(mies, ceny, color='blue', marker='^', s=40)
# plt.xticks(rotation=45)
# plt.yticks(np.arange(0, 4))
# plt.annotate(xy=['listopad', 2.8], text="169415")
# plt.tight_layout()
# plt.subplots_adjust(left=0.1, bottom=0.22, top=0.9)
# plt.xlabel('Miesiąc')
# plt.ylabel('Cena za 1kg')
# plt.title('Wykres cen jabłek w ciągu roku 2016')
#
# plt.savefig('zad2.pdf', format='pdf')
# plt.show()

df = pd.read_excel('turystyka33.xlsx', header=None)
print(df)
df = df.transpose()
df = df.rename(columns=df.iloc[0])
df = df[1:]
df = df.rename(columns={'Nazwa': 'Województwa'})

plt.subplot(1, 2, 1)
sizes1 = df[df['Województwa']=='ŚLĄSKIE'].values
sizes1 = sizes1[0, 1:4]

labels1 = ['Hotele', 'Motele', 'Pensjonaty']
colors1 = ['red', 'blue', 'green']

plt.pie(sizes1, colors=colors1, autopct='%1.1f%%', shadow=True, startangle=90)

plt.title('Wykres dla woj. śląskiego')

plt.axis('equal')
plt.legend(labels=['Hotele', 'Motele', 'Pensjonaty'], loc='lower center')

plt.subplot(1, 2, 2)
sizes2 = df[df['Województwa']=='PODLASKIE'].values
sizes2 = sizes2[0, 1:4]

labels1 = ['Hotele', 'Motele', 'Pensjonaty']
colors1 = ['red', 'blue', 'green']

plt.pie(sizes2, colors=colors1, autopct='%1.1f%%', shadow=True, startangle=90)

plt.title('Wykres dla woj. podlaskiego')

plt.axis('equal')

plt.tight_layout()
plt.savefig('zad3.jpg', format='jpg')
plt.show()