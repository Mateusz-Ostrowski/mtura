'''
4.4 Ostatnie z haseł zostało ukryte w cyfrach zapisanych w pliku napisy.txt. Aby je odczytać,
należy cyfry z każdego wiersza pogrupować po dwie, pomijając ostatnią, jeśli w wierszu jest
nieparzysta liczba cyfr. Jeżeli liczba utworzona przez parę cyfr jest mniejsza od 65 lub większa
od 90, to ją pomijamy, w przeciwnym przypadku taką liczbę zamieniamy na znak o kodzie
ASCII odpowiadającym tej liczbie. Poszukiwanie hasła kończy się po otrzymaniu trzech
kolejnych znaków „X”. Odczytaj z pliku tak ukryte hasło.
Dla danych z pliku przyklad.txt wynikiem jest: NAPISANIEMATURYXXX
'''

lista=[]
with open("napisy.txt") as f:
    for x in f.readlines():
        lista.append(x.strip())

#Zadanie 4.4
haslo=""
for wiersz in lista:
    liczba_1=-1
    liczba_2=-1

    for znak in wiersz:
        if znak.isdigit() and liczba_1 == -1:
            liczba_1 = znak
        elif znak.isdigit():
            liczba_2 = znak
            asci = liczba_1 + liczba_2

            if int(asci)>=65 and int(asci)<=90:
                litera = chr(int(asci))
                haslo+= litera
            liczba_1= -1
            liczba_2= -1
    if haslo.endswith("XXX"):
        break
print(haslo)