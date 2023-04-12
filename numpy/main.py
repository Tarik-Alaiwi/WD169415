import numpy as np

# #inicjalizacja tablicy
# a = np.array([0,1])
# print(a)
#
# #drugi sposob
# a = np.arange(2, 5, 0.1)
# print(a)
#
# #to pokazuje typ zmiennej tablicy, a nie elementow
# print(type(a))
# #a to typ elementow w tablicy
# print(a.dtype)
#
# #inicjalizacja tablicy z konkretnym typem
# a = np.arange(2, dtype='int64')
# print(a.dtype)
#
# #kopia tablicy a z typem float
# b= a.astype('float')
# print(b)
# print(a)
#
# #rozmiar tablicy
# print(a.shape)
#
# #sprawdzenie ilosci wymarow tablicy
# print(a.ndim)
#
# #tablice wielowymiarowa mozna stworzyc przez przekazanie do funkcji array obiektu
#
# zera = np.zeros((5, 5))
# jedynki = np.ones((4, 4))
# print(zera)
# print(jedynki)
#
# print(zera.dtype)
# print(jedynki.dtype)
#
# pusta = np.empty((2,2))
# print(pusta)
#
# macierz = np.array([[12,11], [2, 1]])
# print(macierz)
#
# poz_1 = macierz[1, 1]
# poz_2 = macierz[0][1]
# print(poz_1)
# print(poz_2)

# liczby_lin = np.linspace(1, 2, 5,endpoint=False)
# print(liczby_lin)
#
#
# z = np.indices((5, 3))
# print(z)
# print(z[0][1][0])
#
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
#
# mat_diag_k = np.diag([a for a in range(5)], 1)
# print(mat_diag_k)
#
# z = np.fromiter(range(5), dtype='int32')
# print(z)
#
# znaki = b'ogolna'
# z1= np.frombuffer(znaki, dtype='S1')
# print(z1)
# z2= np.frombuffer(znaki, dtype='S2')
# print(z2)
#
# znaki = 'ogolna'
# z3 = np.array(list(znaki))
# z4 = np.array(list(znaki), dtype='S1')
# z5 = np.array(list(b'ogolna'))
# z6 = np.fromiter(znaki, dtype='S1')
# print(z3)
# print(z4)
# print(z5)
# print(z6)

# a = np.arange(10)
# print(a)
# s = slice(2, 7, 2) #(od, do, krok)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
#
# print(a[2:7:2])
#
# print(a[1:])
# print(a[2:5])

# mat = np.arange(25)
# print(mat)
# mat = mat.reshape((5,5))
# print(mat)
# print(mat[1:]) #od drugiego wiersza
# print(mat[:,1]) #druga kolumna jako wektor
# print(mat[:,1:2]) #macierz 5x1 z drugiej kolumny
# print(mat[:,-1]) #ostatnia kolumna jako wektor
# print(mat[:,4:5]) #ostatnia kolumna jako macierz
# print(mat[2:5, 1:3]) # 2 i 3 kolumna dla 3,4,5 wierszy
# print(mat[:,range(2,6,2)]) # 3 i 5 kolumna
# print(mat[:, [2,4]]) # 3 i 5 kolumna

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]

print(y)
print(x[0,0])
print(x[0,2])
print(x[3,0])
print(x[3,2])