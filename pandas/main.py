import pandas as pd
import numpy as np

# df = pd.read_csv('australian.txt', header=None, sep=' ', decimal='.')
# print(df)

# xlsx = pd.ExcelFile("Wyniki.xlsx")
# df = pd.read_excel(xlsx, header=0)
# print(df)

# #Series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
# print(s)

# #Dataframe
# #tworzenie dataframe na podstawie slownika
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# print(df.dtypes)

# daty = pd.date_range('20210324', periods=5)
# print(daty)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# print(df)

# df = pd.read_csv('zamowienia.csv', sep=";", decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)

# xlsx = pd.ExcelFile("imiona.xlsx")
# df = pd.read_excel(xlsx, header=0)
# print(df)
# df.to_excel('test.xlsx', sheet_name='arkusz pierwszy')

# s = pd.Series([10, 12, 8, 14], index = list('abcd'))
#
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
#
#
# print(s['c'])
# print(s.c)
# print(df[0:1])
# print("")
# print(df['Populacja'])
# print(df.iloc[0, 0])
# print(df.loc[0, "Kraj"])
# print(df.at[0, "Kraj"])
# print("")
# print('kraj: ' + df.Kraj)
# print(df.sample())
# print(df.sample(2))
# print("")
# print(df.sample(frac=0.5))
# print("")
# print(df.sample(n=10, replace=True))
# print("")
# print(df.head())
# print(df.head(1))
# print(df.tail(1))
# print("")
# print(df.describe())
# print(df.T)






# #ZADANIE 1
xlsx = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(xlsx, header=0, skiprows=1)
wynik = 0
for i in df[(df[0]>1999) & (df[0]<2006)][2]:
    wynik += i
print(wynik)