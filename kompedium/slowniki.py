#Slownik to zbior par (klucz-wartosc)
#Skladnia: nazwa_slownika[nazwa_klucza] = wartosc


#Pusty slownik
slownik = {}



#Slownik z wpisanymi od razu jakimis kluzcami i wartosciami
slownik = {"a" : 0, "b" : 0, "c" : 5}

#Wypisanie par klucz wartosc ze slownika
#i to po kolei kazdy klucz
#j to po kolei kazda wartosc
for i,j in slownik.items():
    print(i,j)

#Dopisanie nowego klucza do slownika
slownik["d"] = 10
slownik[1] = "D"
print(slownik)


#Generowanie slownika wystapien liter w danym stringu
s = "adgnmdaghuijhreyonqetyonqetggonjdqgodnaagopnmjadg"
slownik = {}
for c in s:
    if c in slownik:
        #Co sie dzieje gdy element sie powtorzyl
        slownik[c] += 1
    else:
        #Co sie dzieje gdy element wystepuje pierwszy raz
        slownik[c] = 1

for i,j in slownik.items():
    print(i,j)

#Usuwanie klucza ze slownika
slownik.pop("a")
print(slownik)