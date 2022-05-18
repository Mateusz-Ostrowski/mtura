'''
4.3 Palindromem nazywamy napis, który czytany od początku lub od końca jest taki sam (np.
KAJAK). Część napisów zapisanych w wierszach pliku (każdy ma 50 znaków) można w prosty
sposób – przez dodanie dokładnie jednego znaku na początku lub na końcu napisu – zamienić
na palindrom.
Podaj hasło utworzone przez środkowe litery tak utworzonych palindromów.
Dla danych z pliku przyklad.txt wynikiem jest: INFORMATYKA
'''

lista=[]
with open("napisy.txt") as f:
    for x in f.readlines():
        lista.append(x.strip())


haslo=""
for wiersz in lista:

    opcja1 = wiersz+wiersz[0]
    opcja2 = wiersz[len(wiersz)-1]+wiersz

    if opcja1 == opcja1[::-1]:
        haslo += opcja1[(len(opcja1)-1) // 2]
    if opcja2 == opcja2[::-1]:
        haslo+= opcja2[(len(opcja2)-1) // 2]
print()
print(haslo)