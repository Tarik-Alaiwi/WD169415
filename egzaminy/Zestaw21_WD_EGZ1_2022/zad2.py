import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

df = pd.read_excel('ceny21.xlsx')
print(df)

maka_r = df[df['Rodzaje towarów']=='mąka pszenna - za 1kg']['Rok']
maka_w = df[df['Rodzaje towarów']=='mąka pszenna - za 1kg']['Wartość']

kasza_r = df[df['Rodzaje towarów']=='kasza jęczmienna - za 0,5kg']['Rok']
kasza_w = df[df['Rodzaje towarów']=='kasza jęczmienna - za 0,5kg']['Wartość']


plt.scatter(maka_r, maka_w, color='r', marker='o', label='Mąka pszenna')
plt.scatter(kasza_r, kasza_w, color='b', marker='^', label='Kasza jęczmienna')

plt.xlabel('Rok')
plt.ylabel('Cena w zł')
plt.title('Wykres cen mąki pszennej (za 1kg) i kaszy jęczmiennej (za 0,5kg)')
plt.yticks(np.arange(0, 4))
plt.legend(loc='lower left')
plt.annotate(xy=[2018.2, 0.3], text="Tarik")

plt.tight_layout()
plt.savefig('zad2.png', format='png')
plt.show()