'''
Poprawność identyfikatora dokumentu potwierdza pierwsza cyfra z jego numerycznej części,
która jest cyfrą kontrolną.
Podczas sprawdzania poprawności identyfikatora dokumentu litery jego serii są zamieniane na
liczby według następującego przypisania:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35

Aby sprawdzić poprawność identyfikatora danego dokumentu, należy wartość każdego
elementu identyfikatora (poza cyfrą kontrolną) pomnożyć przez odpowiednią wagę. Wagi
poszczególnych składowych identyfikatora to kolejno: 7, 3, 1, 7, 3, 1, 7, 3. Otrzymane iloczyny
należy zsumować i policzyć resztę z dzielenia tej sumy przez 10 (mod 10). Jeśli uzyskana w ten
sposób liczba jest równa wartości pierwszej cyfry z identyfikatora dokumentu, to identyfikator
jest poprawny.
'''

#Odczytujemy z pliku i zapisujemy jako liste stringow
wiersze = []
with open("DANE/identyfikator.txt") as f:
    for s in f.readlines():
        #dodaje zestripowane zeby nie bylo entera na koncu
        wiersze.append(s.strip())


for w in wiersze:
    seria = w[0:3]
    numer = w[3:]
    sumaKontrolna = 0
    #Aby uzyskac A = 10, B = 11 itd bierzemi sobie kod ascii - 55 Bo w ascii A = 65
    #Mnozymy przez odpowiednia wage i dodajemy do sumy kontrolnej
    sumaKontrolna += 7 * (ord(seria[0])-55)
    sumaKontrolna += 3 * (ord(seria[1])-55)
    sumaKontrolna += 1 * (ord(seria[2])-55)
    sumaKontrolna += 7 * int(numer[1])
    sumaKontrolna += 3 * int(numer[2])
    sumaKontrolna += 1 * int(numer[3])
    sumaKontrolna += 7 * int(numer[4])
    sumaKontrolna += 3 * int(numer[5])
    #Sprawdzamy czy reszta z dzielenia przez 10 sumy kontrolnej jest rowna pierwszej cyfrze
    if sumaKontrolna%10 != int(numer[0]):
        print(w)