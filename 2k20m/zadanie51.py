'''
W plikach panstwa.txt, jezyki.txt i uzytkownicy.txt zawarte są informacje
o 40 największych państwach świata, językach świata i ich użytkownikach. Pierwszy wiersz
w każdym z plików jest wierszem nagłówkowym i zawiera nazwy pól. Dane w każdym wierszu
oddzielone są znakami tabulacji.
W pliku panstwa.txt każdy wiersz zawiera informacje o państwach:
Panstwo – nazwa państwa
Kontynent – kontynent, na którym leży stolica państwa
Populacja – całkowita liczba mieszkańców podana w milionach, z dokładnością do
jednego miejsca po przecinku.
Przykład:
Panstwo Kontynent Populacja
Afganistan Azja 32,5
Algieria Afryka 39,7
Argentyna Ameryka Poludniowa 43,4
W pliku jezyki.txt każdy wiersz pliku zawiera informacje o danym języku:
Jezyk – nazwa języka
Rodzina – przynależność języka do rodziny językowej lub określenie „jezyk izolowany”,
jeśli języka nie da się przypisać do żadnej ze znanych rodzin językowych.
Przykład:
Jezyk Rodzina
aceh austronezyjska
acholi nilo-saharyjska
adhola nilo-saharyjska
adi sino-tybetanska
adygejski abchasko-adygijska
W pliku uzytkownicy.txt każdy wiersz zawiera informacje o użytkownikach danego
języka:
Panstwo – nazwa państwa
Jezyk – nazwa języka
Uzytkownicy – liczba posługujących się danym językiem mieszkańców tego państwa
podana w milionach, z dokładnością do jednego miejsca po przecinku
Urzedowy – informacja (tak/nie), czy jest to w danym państwie język urzędowy
Przykład:
Panstwo Jezyk Uzytkownicy Urzedowy
Chiny mandarynski 1212,0 tak
Indie hindi 422,0 tak
USA angielski 255,0 tak
Brazylia portugalski 202,0 tak
Bangladesz bengalski 157,9 tak
Uwaga: w jednym państwie może być kilka języków urzędowych. Dany język może być
językiem urzędowym w jednym państwie, a w innym – nie. Mieszkaniec państwa może
posługiwać się jednym lub wieloma językami.
Strona 5 z 8
MIN_1R
Wykorzystaj dostępne narzędzia informatyczne i podaj odpowiedzi do zadań 5.1.–5.5.
Odpowiedzi zapisz w pliku wyniki5.txt, a każdą z nich poprzedź numerem odpowiedniego
zadania.
'''

'''
Utwórz zestawienie, które dla każdej rodziny językowej podaje, ile języków do niej należy.
Posortuj zestawienie nierosnąco według liczby języków. 
'''


jezyki = []

with open("Dane_PR2/jezyki.txt") as f:
    for s in f.readlines():
        jezyki.append(s.strip())

jezyki.pop(0)
slownikRodzin = {}
for j in jezyki:
    obecnaLista = j.split("\t")
    rodzina = obecnaLista[1]
    if rodzina in slownikRodzin:
        slownikRodzin[rodzina] += 1
    else:
        slownikRodzin[rodzina] = 1

for i,j in slownikRodzin.items():
    print(i,j,sep="\t")