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
Powiemy, że dwa lokale są tego samego rodzaju, jeżeli ich powierzchnia jest taka sama.
W którym mieście powstanie galeria z największą liczbą różnych rodzajów lokali (jest jedno
takie miasto), a w którym powstanie galeria z najmniejszą liczbą różnych rodzajów lokali (jest
jedno takie miasto)? Podaj te miasta oraz liczby różnych rodzajów lokali w tych miastach.
Wynik zapisz w pliku wynik4_3.txt. W każdym z dwóch wierszy pliku powinny znajdować
się nazwa miasta oraz liczba różnych rodzajów lokali w tym mieście.
Prawidłowa odpowiedź dla danych pliku galerie_przyklad.txt:
Dusseldorf 34
Genua 23
'''

#Odczytujemy z pliku i zapisujemy jako liste stringow
wiersze = []
with open("Dane_2103/galerie.txt") as f:
    for s in f.readlines():
        #dodaje zestripowane zeby nie bylo entera na koncu
        wiersze.append(s.strip())

maxLokali = 0
maxMiasto = ""
minLokali = 99999
minMiasto = ""
for w in wiersze:
    #Dzielimy wiersz na liste elmenetow
    lista = w.split()
    #Pary liczb zaczynaja sie od 2 w tej liscie
    paryLiczb = lista[2:]

    listaPowierzchni = []

    for i in range(0,len(paryLiczb),2):
        if int(paryLiczb[i]) == 0:
            break
        listaPowierzchni.append(int(paryLiczb[i])*int(paryLiczb[i+1]))

    #Bierzemy liste bez powtorzen
    powierzchnie = set(listaPowierzchni)
    iloscLokali = len(powierzchnie)
    #Znajdujemy najmniejsza liczbe roznych lokali
    if minLokali > iloscLokali:
        minLokali = iloscLokali
        minMiasto = lista[1]
    #Znajdujemy maksymalna liczbe roznych lokali
    if maxLokali < iloscLokali:
        maxLokali = iloscLokali
        maxMiasto = lista[1]

print(maxMiasto,maxLokali)
print(minMiasto,minLokali)
