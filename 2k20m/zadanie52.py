'''
Podaj liczbę języków, które nie są językami urzędowymi w żadnym państwie. Przy
rozwiązywaniu zadania pamiętaj, że w jednym państwie może być kilka języków urzędowych
oraz że dany język może być językiem urzędowym w jednym państwie, a w innym – nie.
'''

jezyki = []

with open("Dane_PR2/uzytkownicy.txt") as f:
    for s in f.readlines():
        jezyki.append(s.strip())

jezyki.pop(0)
slownikUrzedowych = {}
for j in jezyki:
    obecnaLista = j.split("\t")
    jezyk = obecnaLista[1]
    czyUrzedowy = obecnaLista[3]
    if czyUrzedowy == "tak":
        slownikUrzedowych[jezyk] = "tak"
    else:
        if jezyk not in slownikUrzedowych:
            slownikUrzedowych[jezyk] = "nie"

liczbaJezykow = 0
for i,j in slownikUrzedowych.items():
    if j == "nie":
        liczbaJezykow+=1
print(liczbaJezykow)
