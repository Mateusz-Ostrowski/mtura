'''
Znajdź słowo, w którym występuje największa liczba różnych liter. Wypisz to słowo i liczbę
występujących w nim różnych liter. Jeśli słów o największej liczbie różnych liter jest więcej
niż jedno, wypisz pierwsze z nich pojawiające się w pliku z danymi.
Dla danych z pliku przyklad.txt wynikiem jest:
AKLMNOPRSTWZA 12
'''

wiersze = []
with open("Dane_PR2/sygnaly.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())
wynik = ""
setWyniku = set()

for w in wiersze:
    l = set()
    for c in w:
        l.add(c)
    if len(setWyniku) < len(l):
        setWyniku = l.copy()
        wynik = w

print(wynik,setWyniku)