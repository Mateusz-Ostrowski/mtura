'''
a) Oblicz całkowitą powierzchnię handlową każdej galerii (jako sumę powierzchni wszystkich
lokali w danej galerii) oraz liczbę lokali.
Wyniki zapisz w pliku wynik4_2a.txt. W każdym wierszu pliku wynikowego powinny
się znaleźć: nazwa miasta, powierzchnia galerii znajdującej się w danym mieście oraz
liczba lokali, rozdzielone znakiem spacji.
Dla danych z pliku galerie_przyklad.txt prawidłowa odpowiedź to:

Budapeszt 3598 64
Neapol 3352 48
Marsylia 3444 56
Leeds 2952 44
Frankfurt 3515 57
Genua 3386 56
Dortmund 3697 57
Rotterdam 3184 49
Dusseldorf 3737 63
Kopenhaga 3765 60


b) Podaj nazwę miasta z galerią o największej powierzchni całkowitej oraz nazwę miasta
z galerią o najmniejszej powierzchni całkowitej. Jest dokładnie jedno miasto z galerią
o największej powierzchni i jedno z galerią o najmniejszej powierzchni.
Wyniki zapisz w pliku wynik4_2b.txt. W pliku wynikowym powinny znaleźć się nazwy
miast wraz z powierzchniami galerii.
Prawidłowa odpowiedź dla danych pliku galerie_przyklad.txt:
Kopenhaga 3765
Leeds 2952

'''

#Odczytujemy z pliku i zapisujemy jako liste stringow
wiersze = []
with open("Dane_2103/galerie.txt") as f:
    for s in f.readlines():
        #dodaje zestripowane zeby nie bylo entera na koncu
        wiersze.append(s.strip())

minMiasto = ""
minPowierzchnia = 9999999

maxMiasto = ""
maxPowierzchnia = 0

for w in wiersze:
    #Dzielimy wiersz na liste elmenetow
    lista = w.split()
    #Pary liczb zaczynaja sie od 2 w tej liscie
    paryLiczb = lista[2:]

    #Liczymy liczbe lokali czyli dopoki powierzchnia jest rozna od 0
    liczbaLokali = 0
    polePowierzchni = 0
    for i in range(0,len(paryLiczb),2):
        if int(paryLiczb[i]) == 0:
            break
        #Dodajemy iloczyn dwoch kolejnych do pola
        polePowierzchni += (int(paryLiczb[i]) * int(paryLiczb[i+1]))

        #Znaleziono kolejny lokal wiec dodajemy 1
        liczbaLokali += 1

    #znajdujemy minimalna powierzchnie
    if minPowierzchnia > polePowierzchni:
        minPowierzchnia = polePowierzchni
        minMiasto = lista[1]

    #Znajdujemy maksymalna powierczhnie
    if maxPowierzchnia < polePowierzchni:
        maxMiasto = lista[1]
        maxPowierzchnia = polePowierzchni

    print(lista[1], polePowierzchni, liczbaLokali)

print()
print("Min",minMiasto,minPowierzchnia)
print("Max",maxMiasto,maxPowierzchnia)