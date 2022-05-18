'''
Znajdź 6 języków, którymi posługuje się łącznie najwięcej mieszkańców obu Ameryk
(„Ameryka Polnocna” i „Ameryka Poludniowa”), a które nie należą do rodziny
indoeuropejskiej („indoeuropejska”). Dla każdego z nich podaj nazwę, rodzinę językową
i liczbę użytkowników w obu Amerykach łącznie.
'''

jezyki = []

with open("Dane_PR2/jezyki.txt") as f:
    for s in f.readlines():
        jezyki.append(s.strip())

uzytkownicy = []

with open("Dane_PR2/uzytkownicy.txt") as f:
    for s in f.readlines():
        uzytkownicy.append(s.strip())

uzytkownicy.pop(0)
jezyki.pop(0)
panstwaAmeryk = ["Argentyna","Brazylia","Kanada","Kolumbia","Meksyk","USA"]
slownikJezykRodzina = {}
for j in jezyki:
    obecnaLista = j.split("\t")
    jezyk = obecnaLista[0]
    rodzina = obecnaLista[1]
    slownikJezykRodzina[jezyk] = rodzina

slownikJezykUzytkownicy = {}
for u in uzytkownicy:
    obecnaLista = u.split("\t")
    jezyk = obecnaLista[1]
    panstwo = obecnaLista[0]
    liczbaUzytkownikow = float(obecnaLista[2].replace(",","."))
    if panstwo in panstwaAmeryk and slownikJezykRodzina[jezyk] != "indoeuropejska":
        if jezyk in slownikJezykUzytkownicy:
            slownikJezykUzytkownicy[jezyk] += liczbaUzytkownikow
        else:
            slownikJezykUzytkownicy[jezyk] = liczbaUzytkownikow
for i,j in slownikJezykUzytkownicy.items():
    print(i,slownikJezykRodzina[i],str(round(j,2)).replace(".",","),sep="\t")
