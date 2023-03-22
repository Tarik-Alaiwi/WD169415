
# plik = open("tekst.txt", "r", encoding='utf8')#odczyt 10 znaków
# znaki = plik.read(10)
# #odczyt jednej lini z pliku
# linia = plik.readline() #odczyt wierszy z pliku
# wiersze = plik.readlines() #zamknięcie pliku
# plik.close()#drukujemy 10 znaków
# print(znaki)
# print(linia)
# print(wiersze)

# with open("tekst.txt", "r", encoding='utf8') as plik:
#     for linia in plik:
#         print(linia, end="")

# ZADANIE 1
# A = [x for x in range(0, 31)]
# B = [x*2 for x in A]
# plik = open("dane.txt", "w+")
# plik.writelines(str(B))
# plik.close()

#ZADANIE 2
# plik = open("dane.txt", "r", encoding='utf8')
# linia = plik.readline()
# plik.close()
# print(linia)

#ZADANIE 3
# # Zapisz kilka linii tekstu do pliku
# with open("dane.txt", "a") as plik:
#     plik.write("\nTo jest pierwsza linia tekstu.\n")
#     plik.write("To jest druga linia tekstu.\n")
#     plik.write("To jest trzecia linia tekstu.\n")
#
# # Otwórz plik i wyświetl jego zawartość na ekranie
# with open("dane.txt", "r") as plik:
#     print(plik.read())

#ZADANIE 4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print(f"Produkt: {self.nazwa_produktu}, cena: {self.cena_jed} zł/{self.jednostka_miary}")
#
#     def ile_produktu(self):
#         return f"{self.ilosc} {self.jednostka_miary}"
#
#     def ile_kosztuje(self):
#         a = self.ilosc * self.cena_jed
#         return f"{a} zl"
#
# ziemniaki = NaZakupy("ziemniaki", 3, "kg", 2.5)
# ziemniaki.wyswietl_produkt() # wyświetli "Produkt: ziemniaki, cena: 2.5 zł/kg"
# print(ziemniaki.ile_produktu()) # wyświetli "3 kg"
# print(ziemniaki.ile_kosztuje()) # wyświetli 7.5 (czyli 3 * 2.5)

class PierwszaKlasa:
    """Pierwsza klasa python"""
    atrybut = 54321
    def pierwsza_metoda(self):
        return "Teraz działa pierwsza Metoda"

obiekt = PierwszaKlasa()
print(obiekt)
print(obiekt.atrybut)
print(obiekt.pierwsza_metoda())