'''
Podaj, ile było kursów, w których statek spędził więcej niż 20 pełnych dni na morzu, bez
zawijania do portów.
Przykład:
Jeśli statek wypłynął z jednego portu w dniu 2016-01-10 i wpłynął do następnego portu w dniu
2016-01-16, to spędził na morzu 5 pełnych dni (11.01, 12.01, 13.01, 14.01, 15.01).
'''

from datetime import date

wiersze = []
with open("Dane_PR2/statek.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

wiersze.pop(0)

licznik = 0
for i in range(1,len(wiersze)):
    obecnaLista = wiersze[i].split("\t")
    poprzedniaLista = wiersze[i-1].split("\t")
    obecnaData = date.fromisoformat(obecnaLista[0])
    poprzedniaData = date.fromisoformat(poprzedniaLista[0])
    roznica = obecnaData-poprzedniaData
    if roznica.days >= 21:
        licznik += 1
print(licznik)


