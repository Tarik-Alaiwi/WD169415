import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

plt.subplot(2, 2, 1)

sizes1 = [15.7, 25.58, 16.86, 21.51, 12.79, 7.56]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['saddlebrown', 'hotpink', 'tan', 'lawngreen', 'saddlebrown', 'royalblue']
explode1 = (0, 0.1, 0, 0, 0, 0)

plt.pie(sizes1, explode=explode1, labels=labels, colors=colors, autopct='%1.2f%%', startangle=45)

plt.title('Lewo Góra')
plt.axis('equal')

plt.subplot(2, 2, 4)

sizes2 = [20.37, 17.59, 9.72, 19.91, 15.74, 16.67]
labels = ['A', 'B', 'C', 'D', 'E', 'F']
colors = ['saddlebrown', 'hotpink', 'tan', 'lawngreen', 'saddlebrown', 'royalblue']
explode2 = (0, 0.08, 0, 0, 0, 0)

plt.pie(sizes2, explode=explode2, labels=labels, colors=colors, autopct='%1.2f%%', startangle=45)

plt.title('Prawo Dół')
plt.axis('equal')

plt.tight_layout()
plt.savefig('zad1.jpg', format='jpg')
plt.show()