#Stworzenie nowej pustej listy
moja_lista = []

#Stworzenie nowej 3 elementowej listy i wypełnienie jej od razu 1,2,3
moja_lista2 = [1,2,3]

#Listy indeksowane sa od 0
print("Odwolywanie sie do konkretnych elementów: ")
print(moja_lista2[0],moja_lista2[1],moja_lista2[2])

#Przechodzenie przez cala liste

#W tym przypadku i to pokolei każdy element listy
#Przydante gdy przechodzimy element po elemencie bez potrzeby zaglądania do sąsiednich elementów
for i in moja_lista2:
    #Coś robimy
    print(i)

#W tym przypadku i to indeks elementu, a j to element o indeksie i
#Przydatne gdy potrzebujemy np dwóch kolejnych elementów
#i przyjmuje pokolei od 0 do (dlugosci listy - 1)
for i in range(0,len(moja_lista2)):
    #Coś robimy
    j = moja_lista2[i]
    print(i,j)

#Przyklad gdy lista nie zawiera samych liczb
def sumaElementowListy(l):
    #Suma elementów listy
    suma = 0
    for i in l:
        #zwieksz sume o i
        suma += int(i)
    return suma

#Przyklad gdy lista zawiera same liczby
suma = sum(moja_lista2)
print(suma)

'''
Dodawanie elementow do listy
'''
print(moja_lista)

#Dodaje 1 na koniec moja_lista
moja_lista.append(1)
#Dodaje 2 na koniec moja_lista
moja_lista.append(2)
#itd.
moja_lista.append(3)

print(moja_lista)

#Przechodzimy od 0 do 999 włącznie
for i in range(0,1000):
    #Dodaje 1000 zer na koniec listy
    moja_lista.append(0)

#Dodaje i czyli po kolei liczby od 0 do 999 do listy
for i in range(0,1000):
    moja_lista.append(i)

#Przechodzenie wyraz po wyrazie
listaStringow = ["123", "TEST", "ATDETADTADTAD", "TQETQET"]
for i in listaStringow:
    #Coś robimy
    print(i)

#Przechodzenie wyraz po wyrazie
for i in listaStringow:
    #Przechodzenie litera po literze przez stringa ktorym jest i
    for j in i:
        #Coś robimy
        print(j)

#Sprawdzanie czy element zawiera sie w liscie
if "123" in listaStringow:
    #cos robimy
    print("Zawiera sie")
else:
    #cos innego robimy
    print("Nie zawiera sie")

if "costam" not in listaStringow:
    #cos robimy
    print("Nie zawiera sie")

#Laczenie dwoch list (dolacza na koniec moja_lista elementy moja_lista2)
moja_lista += moja_lista2
print(moja_lista)

#Sortuje moja_lista o ile są tam wartosci tego samego typu (same liczby albo same napisy)
moja_lista.sort()
print(moja_lista)

#Skopiowanie wycinka listy

#Kopiuje wycinek listy zlozony z pierwszych 5 elementow o indeksach (0,1,2,3,4)
wycinek = moja_lista[0:5]
print(wycinek)

#Kopiuje wycinek listy  od 2000 elementu do ostatniego (jeśli nie podamy indeksu po : to bierze ostatni)
wycinek = moja_lista[2000:]
print(wycinek)

#Kopiuje liste i ją odwraca
odwrocona = wycinek[::-1]
print(odwrocona)


#Sprawdzanie czy dwie listy mają takie same elementy w tej samej kolejnosci
lista1 = [1,2,3,4,5]
lista2 = [1,2,3,4,5]
if lista1 == lista2:
    print("TE same elementy")

'''
Sprawdzanie czy wszystkie elementy z listy1 znajduja sie w liscie2
'''
lista1 = [4,7,1,9]
lista2 = [1,2,3,4,5,6,7,8]

#Zakladamy ze wszystkie elementy sie znajduja
znajdujaSie = True
for i in lista1:
    #Jesli znajdziemy taki ktory sie nie znajduje to przestawiamy na false
    if i not in lista2:
        znajdujaSie = False

#Dalej zaleznie czy znajdowaly czy nie cos robimy
if znajdujaSie:
    print("Wszystkie elementy z listy1 sa w liscie2")
else:
    print("Nie wszystkie elementy z listy1 sa w liscie2")


#Sprawdzanie czy lista posiada podliste o okreslonych elemntach
lista1 = [1,2,3,4,5,6,7]
wycinek = [2,3,4]
dlWycinka = len(wycinek)
for i in range(0,len(lista1)-dlWycinka+1):
    if lista1[i:i+dlWycinka] == wycinek:
        print("Znaleziono kolejne elementy: ",wycinek,i)



#Jesli mamy dwie listy o takiej samej dlugosci i chcemy przejsc przez dwie naraz
lista1 = [1,2,3,4,5]
lista2 = [0,0,0,-8,1]

#Policzmy sume odpowiadajcych sobie elementow pod tym samym indeksem
for i in range(0,len(lista1)):
    e1 = lista1[i]
    e2 = lista2[i]
    print(e1+e2,end=" ")
print()

#Odczytujmy co n-ty element z listy i zacznijmy na 5
n = 4
lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for i in range(5,len(lista1),n):
    e = lista1[i]
    print(e,end=" ")
print()

'''
Rozdzienialnie stringa na liste elementow
'''

#Rozdzielanie po spacji
s = "5 123 544 243 123 1230 53"
lista = s.split()
print(lista)

#Dla jakis znakow (sredniki,przecinki itd)
s = "5;123;544;243;123;1230;53"
lista = s.split(";")
print(lista)

#Dla tabulatorow
s = "5\t123\t544\t243\t123\t1230\t53"
lista = s.split("\t")
print(lista)

'''
Laczenie elementow listy w jednego stringa
'''

#Elementy nie beda oddzielone
lista = ["1","2","3","4","5","6"]
napis = "".join(lista)
print(napis)

#Elementy beda oddzielone ciagiem znakow ;|,
lista = ["1","2","3","4","5","6"]
napis = ";|,".join(lista)
print(napis)

#Laczenie gdy lista zawiera liczby zamiast stringow
lista = [1,2,3,4,5,6]
napis = ""
separator = ";|,"
for x in lista:
    napis += str(x) + separator
print(napis[0:len(napis)-len(separator)])

'''
Usuwanie elemntow
'''

#Usuniecie elementu o danym indeksie np. 4 (usuwa i przesuwa elementy z prawej do lewej)
lista = [0,1,2,3,4,5,6,7]
lista.pop(4)
print(lista)

#Usuniecie ostatniego elementu
lista = [0,1,2,3,4,5,6,7]
lista.pop()
print(lista)

'''
Znajdywanie najdluzszych ciagow czegos
'''

#Najdluzszy ciag tych samych stringow (pierwszy wystepujacy)
lista = ["123","433","123","123","a","a","a","a","123","123","123","123"]

#Ciag ktory resetujemy gdy znajdziemy element nie rowny poprzedniemu
obecnyCiag = []
#Ciag ktory ustawiamy gdy obecny ciag jest dluzszy od niego
najdluszyCiag = []

for w in lista:
    if w not in obecnyCiag:
        obecnyCiag = [w]
    else:
        obecnyCiag.append(w)

    if len(najdluszyCiag) < len(obecnyCiag):
        najdluszyCiag = obecnyCiag

print(najdluszyCiag)


#Zwraca indeks elementu ktory przekazemy
lista = [5,7,13,5353,213]
print(lista.index(13))

#Zlicza wystapienie w liscie danego elementu np ilosc piątek
lista = [5,7,3,2,1,4,5,6,7,8,4,5]
print(lista.count(5))

