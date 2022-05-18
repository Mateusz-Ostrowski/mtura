'''
Dla każdego słowa z pliku pary.txt znajdź długość najdłuższego spójnego fragmentu tego
słowa złożonego z identycznych liter. Wypisz znalezione fragmenty słów i ich długości
oddzielone spacją, po jednej parze w każdym wierszu. Jeżeli istnieją dwa fragmenty o takiej
samej największej długości, podaj pierwszy z nich. Wyniki podaj w kolejności zgodnej
z kolejnością danych w pliku pary.txt.
Przykład:
dla słowa zxyzzzz wynikiem jest:
zzzz 4
natomiast dla słowa kkkabbb wynikiem jest:
kkk 3
Dla danych z pliku przyklad.txt odpowiedzi podano w pliku odp_przyklad.txt.
'''

wiersze = []

with open("Dane_PR2/pary.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

for w in wiersze:
    obecnaLista = w.split(" ")
    wyraz = obecnaLista[1]
    najdluzszyCiagLiter = ""
    obecnyCiagLiter = ";"
    for c in wyraz:
        if c == obecnyCiagLiter[0]:
            obecnyCiagLiter += c
        else:
            obecnyCiagLiter = c
        if len(najdluzszyCiagLiter) < len(obecnyCiagLiter):
            najdluzszyCiagLiter = obecnyCiagLiter
    print(najdluzszyCiagLiter,len(najdluzszyCiagLiter))

