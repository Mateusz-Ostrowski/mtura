'''
W dniach 2016-02-01 i 2018-08-01 statek nie zawijał do portu.
Dla każdego z tych dni podaj:
• rodzaj i liczbę ton towaru, którego było najwięcej na statku,
• rodzaj i liczbę ton towaru, którego było najmniej na statku (przyjmujemy, że towar był na
statku, jeśli liczba ton tego towaru była większa od 0).
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
    data = obecnaLista[0]
    if zaladunek == "Z":
        if towar not in slownikTowarow:
            slownikTowarow[towar] = masa
        else:
            slownikTowarow[towar] += masa
    else:
        slownikTowarow[towar] -= masa
    print(data,slownikTowarow)


