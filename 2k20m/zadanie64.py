'''
Sporządź wykres kolumnowy przedstawiający, ile załadowano i ile wyładowano towaru T5
w każdym miesiącu od 1 stycznia 2016 r. do 18 grudnia 2018 r. Załadunek i wyładunek dla
każdego miesiąca przedstaw w dwóch kolumnach. Pamiętaj o opisaniu obu osi (dla osi
poziomej użyj formatu rrrr-mm) i o tytule wykresu.
'''

wiersze = []
with open("Dane_PR2/statek.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

wiersze.pop(0)
slownikMiesiaceZW = {}

for w in wiersze:
    listaOBecna = w.split("\t")
    rokMiesiac = listaOBecna[0][0:7]
    rodzaj = listaOBecna[2]
    zaladunek = listaOBecna[3]
    tony = int(listaOBecna[4])
    if rodzaj == "T5":
        if zaladunek == "W":
            if rokMiesiac in slownikMiesiaceZW:
                slownikMiesiaceZW[rokMiesiac][0] += tony
            else:
                slownikMiesiaceZW[rokMiesiac] = [tony,0]
        else:
            if rokMiesiac in slownikMiesiaceZW:
                slownikMiesiaceZW[rokMiesiac][1] += tony
            else:
                slownikMiesiaceZW[rokMiesiac] = [0,tony]
for i,j in slownikMiesiaceZW.items():
    print(i,j[0],j[1])
