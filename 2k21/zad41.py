'''W pliku napisy.txt znajduje się 1000 wierszy po 50 znaków (dużych liter angielskiego
alfabetu oraz cyfr).
Napisz program(y), który(e) da(dzą) odpowiedzi do poniższych zadań. Odpowiedzi zapisz
w pliku wyniki4.txt, a każdą odpowiedź poprzedź numerem oznaczającym odpowiednie
zadanie.
Uwaga: Plik przyklad.txt zawiera dane przykładowe spełniające warunki zadania.
Odpowiedzi dla danych z pliku przyklad.txt są podane pod pytaniami.

4.1 Podaj łączną liczbę cyfr we wszystkich napisach z pliku napisy.txt.
Dla danych z pliku przyklad.txt wynikiem jest: 46504
'''

lista=[]
with open("napisy.txt") as f:
    for x in f.readlines():
        lista.append(x.strip())
#Zadanie 4.1
licznik=0
for wiersz in lista:
    for i in wiersz:
        if i.isdigit():
            licznik+=1
print("Zadanie 4.1 wynik: ", licznik)





