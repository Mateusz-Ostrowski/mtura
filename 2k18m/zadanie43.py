'''
W tym zadaniu rozważmy odległość liter w alfabecie – np. litery A i B są od siebie oddalone
o 1, A i E o 4, F i D o 2, a każda litera od siebie samej jest oddalona o 0. Wypisz wszystkie
słowa, w których każde dwie litery oddalone są od siebie w alfabecie co najwyżej o 10. Słowa
wypisz w kolejności występowania w pliku sygnaly.txt, po jednym w wierszu.
Na przykład CGECF jest takim słowem, ale ABEZA nie jest (odległość A – Z wynosi 25).

Dla danych z pliku przyklad.txt wynikiem jest :
AAAAAAAAAI
AAAAAAAAAE
AAAAAAAAAC
AAAAAAAAAH
AAAAAAAAAC
AAAAAAAAAI
AAAAAAAAAA
BB
AAAAAAAAAA
AAAAAAAAAA
AAAAAAAAAB
AAAAAAAAAE
AAAAAAAAAD
AAAAAAAAAI
AAAAAAAAAE
'''

wiersze = []
with open("Dane_PR2/sygnaly.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

for w in wiersze:
    czyWyraz = True
    for i in range(0,len(w)-1):
        for j in range(i+1,len(w)):
            if abs(ord(w[i])-ord(w[j])) > 10:
                czyWyraz = False
                break
    if czyWyraz:
        print(w)