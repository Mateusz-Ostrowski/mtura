'''
Podaj wszystkie te identyfikatory dokumentów z pliku identyfikator.txt, których seria
lub numer są palindromami, czyli czytane od lewej do prawej i od prawej do lewej są takie
same. Odpowiedź zapisz w pliku wyniki4_2.txt, po jednym identyfikatorze w wierszu,
w kolejności zgodnej z kolejnością w pliku identyfikator.txt.
Prawidłowa odpowiedź dla pliku identyfikator_przyklad.txt:
KOK201272
PIP417543
MOS302203
'''

#Odczytujemy z pliku i zapisujemy jako liste stringow
wiersze = []
with open("DANE/identyfikator.txt") as f:
    for s in f.readlines():
        #dodaje zestripowane zeby nie bylo entera na koncu
        wiersze.append(s.strip())

#Przechodzimy przez wiersze
for w in wiersze:
    #Bierzemy pierwsze litery serii
    seria = w[0:3]
    #Bierzemy reszted jako numer
    numer = w[3:]
    #Sprawdzamy czy numer jest rowny odwrotnemu numerowi lub seria jest rowna odwrotnej serii
    if numer == numer[::-1] or seria == seria[::-1]:
        print(w)

