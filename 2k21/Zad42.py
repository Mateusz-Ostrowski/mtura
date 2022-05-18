'''
4.2 W pliku napisy.txt ukryto pewne pięćdziesięcioznakowe hasło w następujący sposób:
– w co dwudziestym wierszu (w wierszach o numerach 20, 40, 60, …, 1000), ukryto dokładnie
jedną literę hasła;
– ukryta litera w kolejnych wierszach zawsze znajduje się na innej pozycji: w 20 wierszu na
pierwszej, w 40 wierszu na drugiej, w 60 wierszu na trzeciej, …, w 1000 na pięćdziesiątej.
Podaj to hasło.
Dla danych z pliku przyklad.txt wynikiem jest:
UDALOSIEIZDAJEMYEGZAMINYMATURALNEZWIELUPRZEDMIOTOW
'''
lista=[]
with open("napisy.txt") as f:
    for x in f.readlines():
        lista.append(x.strip())

#Zadanie 4.2
haslo=""
index=0
for i in range(19,len(lista),20):
    haslo += lista[i][index]
    index+=1
print(haslo)