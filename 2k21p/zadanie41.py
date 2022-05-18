'''
Firma Igloo planuje w wybranych miastach Europy wybudować galerie handlowe. W każdej
z planowanych galerii może znajdować się różna liczba lokali handlowych. Wszystkie lokale
handlowe będą miały kształt prostokąta.
W pliku galerie.txt zapisanych jest 50 wierszy z informacjami dotyczącymi planowanych
galerii. Każdy wiersz w pliku to informacja o jednej galerii. Dane oddzielone są spacją
i zawierają odpowiednio:
- kod kraju;
- nazwę miasta (nazwy miast nie powtarzają się);
- 70 par liczb (140 liczb) określających wymiary (długość i szerokość w metrach) lokali
handlowych, które znajdować się będą w danej galerii. Jeżeli liczba lokali w galerii jest
mniejsza niż 70, to wiersz uzupełniony jest zerami.
Przykład:
NL Amsterdam 8 4 5 12 7 5 5 11 9 4 7 6 … 0 0 0 0 0 0
Do Twojej dyspozycji jest pomocniczy plik galerie_przyklad.txt, zawierający
10 wierszy, który możesz wykorzystać, aby sprawdzić poprawność działania swojego(-ich)
programu(-ów).
Napisz program(-y), w wyniku działania którego(-ych) otrzymasz odpowiedzi do podanych
zadań. Pliki źródłowe z rozwiązaniem zapisz pod nazwą zgodną z numerem zadania,
z rozszerzeniem odpowiadającym użytemu narzędziu informatycznemu.
'''

'''
Dla każdego kraju z pliku galerie.txt wyznacz liczbę miast, w których powstaną galerie.
Wynik zapisz w pliku wynik4_1.txt. W każdym wierszu pliku powinny znajdować się: kod
państwa oraz informacja o liczbie miast.
Dla danych z pliku galerie_przyklad.txt prawidłowa odpowiedź to:
H 1
I 2
F 1
GB 1
D 3
NL 1
DK 1
'''

#Odczytujemy z pliku i zapisujemy jako liste stringow
wiersze = []
with open("Dane_2103/galerie.txt") as f:
    for s in f.readlines():
        #dodaje zestripowane zeby nie bylo entera na koncu
        wiersze.append(s.strip())

slownik = {}

for w in wiersze:
    lista = w.split()
    kod = lista[0]
    #Natrafiamy znowu na kod ten sam zwiekszamy wystpiaenia o 1
    if kod in slownik:
        slownik[kod] += 1
    #Natrafiamy na kod pierwszy raz ustawiamy wystapienia na 1
    else:
        slownik[kod] = 1

#Wypisujemy ze slownika pary kod,wystapienie
for i,j in slownik.items():
    print(i,j)