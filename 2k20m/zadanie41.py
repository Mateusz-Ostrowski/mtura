'''
W pliku pary.txt znajduje się 100 wierszy. Każdy wiersz zawiera parę danych składającą
się z liczby całkowitej z przedziału od 3 do 100 i słowa (ciągu znaków) złożonego z małych
liter alfabetu angielskiego o długości od 1 do 50 znaków. Liczba i słowo są oddzielone znakiem
spacji.
Napisz program(-my), dający(-e) odpowiedzi do poniższych zadań. Uzyskane odpowiedzi
zapisz w pliku wyniki4.txt, poprzedzając każdą z nich numerem odpowiedniego zadania.
Uwaga: plik przyklad.txt zawiera przykładowe dane spełniające warunki zadania.
Odpowiedzi dla danych z pliku przyklad.txt są podane pod treściami zadań oraz w pliku
odp_przyklad.txt.
'''

'''
Mocna hipoteza Goldbacha mówi, że każda parzysta liczba całkowita większa od 4 jest sumą
dwóch nieparzystych liczb pierwszych, np. liczba 20 jest równa sumie 3 + 17 lub sumie
7 + 13.
Każdą liczbę parzystą z pliku pary.txt przedstaw w postaci sumy dwóch liczb pierwszych.
Wypisz tę liczbę oraz dwa składniki sumy w kolejności niemalejącej. Jeżeli istnieje więcej
rozwiązań (tak jak dla liczby 20) należy wypisać składniki sumy o największej różnicy.
Wyniki podaj w oddzielnych wierszach, w kolejności zgodnej z kolejnością danych w pliku
pary.txt. Liczby w każdym wierszu rozdziel znakiem spacji, np. dla liczby 20 należy
wypisać 20 3 17.
Dla danych z pliku przyklad.txt prawidłową odpowiedzią jest:
24 5 19
6 3 3
6 3 3 
'''

wiersze = []

with open("Dane_PR2/pary.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

def czy_pierwsza(n):
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    return True

for w in wiersze:
    obecnaLista = w.split()
    liczba = int(obecnaLista[0])
    j = 3
    if liczba % 2 == 0:
        while j < liczba:
            i = liczba - 3
            while i > liczba // 2:
                if czy_pierwsza(i) and czy_pierwsza(j) and i + j == liczba:
                    break
                i-=1
            if czy_pierwsza(i) and czy_pierwsza(j) and i + j == liczba:
                break
            j+=1
        print(liczba,j,i)

