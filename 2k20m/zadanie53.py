'''
Podaj wszystkie języki, którymi posługują się użytkownicy na co najmniej czterech
kontynentach.
Uwaga: dla uproszczenia przyjmujemy, że państwo leży na tym kontynencie, na którym
znajduje się jego stolica.
'''

panstwa = []

with open("Dane_PR2/panstwa.txt") as f:
    for s in f.readlines():
        panstwa.append(s.strip())

uzytkownicy = []

with open("Dane_PR2/uzytkownicy.txt") as f:
    for s in f.readlines():
        uzytkownicy.append(s.strip())

uzytkownicy.pop(0)
panstwa.pop(0)

slownikKontynentPanstwo = {}
for p in panstwa:
    obecnaLista = p.split("\t")
    panstwo = obecnaLista[0]
    kontynent = obecnaLista[1]
    slownikKontynentPanstwo[panstwo] = kontynent
slownikJezykow = {}

for u in uzytkownicy:
    obecnaLista = u.split("\t")
    panstwo = obecnaLista[0]
    jezyk = obecnaLista[1]
    if jezyk not in slownikJezykow:
        slownikJezykow[jezyk] = [slownikKontynentPanstwo[panstwo]]
    else:
        slownikJezykow[jezyk].append(slownikKontynentPanstwo[panstwo])

for i,j in slownikJezykow.items():
    if len(set(j)) >= 4:
        print(i)