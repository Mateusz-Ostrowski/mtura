'''
Naukowcy zauważyli, że po złączeniu dziesiątych liter co czterdziestego słowa (zaczynając od
słowa czterdziestego) otrzymamy pewne przesłanie. Wypisz to przesłanie.
Uwaga: Każde co czterdzieste słowo ma co najmniej 10 znaków.
Dla danych z pliku przyklad.txt wynikiem jest:
NIECHCIMATURAPROSTABEDZIE
'''

wiersze = []
with open("Dane_PR2/sygnaly.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())
wynik = ""
for i in range(39,1000,40):
    wynik += wiersze[i][9]
print(wynik)