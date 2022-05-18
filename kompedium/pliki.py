#Przykład otworzenia pliku i wczytania kazdego wiersza do listy


#Składnia open(sciezka_do_pliku)
#sciezka_do_pliku jest wzgledna do pliku na ktorym pracujemy
#jesli jestesmy w folderze MATURA_KOMPEDIUM_WIEDZY to pod nia jest folder z plikiem txt

wiersze = []

with open("folder/plik.txt") as f:
    #Przechodzimy przez każdą linijke i dodajemy do listy ta linijke bez znaku entera
    for s in f.readlines():
        wiersze.append(s.strip())

#Dalsze działania możemy prowadzić już przechodząc przez liste wierszy
#UWAGA wszystkie elementy tej listy to stringi więc przy obliczeniach trzeba zamieniać na int'a lub float'a

for w in wiersze:
    print(w)