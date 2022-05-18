'''
Para (liczba1, słowo1) jest mniejsza od pary (liczba2, słowo2), gdy:
– liczba1 < liczba2,
albo
– liczba1 = liczba2 oraz słowo1 jest leksykograficznie (w porządku alfabetycznym)
mniejsze od słowo2.
Przykład:
para (1, bbbb) jest mniejsza od pary (2, aaa), natomiast para (3, aaa) jest mniejsza od pary
(3, ab).
Rozważ wszystkie pary (liczba, słowo) zapisane w wierszach pliku pary.txt, dla których
liczba jest równa długości słowa, i wypisz spośród nich taką parę, która jest mniejsza od
wszystkich pozostałych. W pliku pary.txt jest jedna taka para.
Dla danych z pliku przyklad.txt odpowiedzią jest:
6 abbbbc
'''

wiersze = []

with open("Dane_PR2/pary.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())


liczbaMin = 999999999
wyrazMin = ""
for w in wiersze:
    obecnaLista = w.split()
    liczba = int(obecnaLista[0])
    wyraz = obecnaLista[1]
    if len(wyraz) == liczba:
        if liczbaMin > liczba:
            liczbaMin = liczba
            wyrazMin = wyraz
        elif liczbaMin == liczba and wyraz < wyrazMin:
            liczbaMin = liczba
            wyrazMin = wyraz
print(liczbaMin,wyrazMin)