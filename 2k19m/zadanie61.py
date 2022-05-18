'''
Podaj jasność najjaśniejszego i jasność najciemniejszego piksela.
Dla danych z pliku przyklad.txt wynikiem jest 255 (najjaśniejszy) i 0 (najciemniejszy).
'''

wiersze = []
with open("Dane_PR2/dane.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

minPixel = 255
maxPixel = 0
for w in wiersze:
    listaPixeli = w.split()
    for p in listaPixeli:
        if int(p) < minPixel:
            minPixel = int(p)
        if int(p) > maxPixel:
            maxPixel = int(p)
print(minPixel,maxPixel)