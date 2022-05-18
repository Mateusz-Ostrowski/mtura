'''
Podaj, który towar był ładowany na statek najwięcej razy i jaka była łączna masa tych
załadunków.
'''

wiersze = []
with open("Dane_PR2/statek.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

wiersze.pop(0)

slownikTowarow = {}
for w in wiersze:
    obecnaLista = w.split("\t")
    towar = obecnaLista[2]
    zaladunek = obecnaLista[3]
    masa = int(obecnaLista[4])
    if zaladunek == "Z":
        if towar not in slownikTowarow:
            slownikTowarow[towar] = [1, masa]
        else:
            slownikTowarow[towar][0] += 1
            slownikTowarow[towar][1] += masa

for i,j in slownikTowarow.items():
    print(i,j)