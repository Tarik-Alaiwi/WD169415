import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

df = pd.read_csv('wynagrodzenia21.csv', sep=';', decimal=',')
print(df)
df = df.melt(id_vars='Województwo', var_name='Rok', value_name='Ilość')

wm = df[(df['Województwo']=='WARMIŃSKO-MAZURSKIE') & ((df['Rok']=='2010') | (df['Rok']=='2011')
        | (df['Rok']=='2012') | (df['Rok']=='2013'))]['Ilość']

maz = df[(df['Województwo']=='MAZOWIECKIE') & ((df['Rok']=='2010') | (df['Rok']=='2011')
        | (df['Rok']=='2012') | (df['Rok']=='2013'))]['Ilość']
Y = np.arange(4)

plt.barh(Y + 0.00, wm, color='b', height=0.25, label="Warmińsko-Mazurskie")
plt.barh(Y + 0.25, maz, color='g', height=0.25, label="Mazowieckie")

labelsbar = np.arange(2010, 2014)
plt.yticks(Y + 0.125, labelsbar)
plt.ylabel('Rok')
plt.xlabel('Ilość')
plt.legend()
plt.title('Wykres wybranych województw na przestrzeni lat')
plt.tight_layout()

plt.savefig('zad3.pdf', format='pdf')
plt.show()