'''
Plik identyfikator.txt zawiera 200 wierszy. W każdym wierszu jest zapisany
identyfikator pewnego dokumentu, który składa się z serii (trzy wielkie litery alfabetu
łacińskiego) oraz sześciu cyfr.
Napisz program(-y), w wyniku działania którego(-ych) otrzymasz odpowiedzi do poniższych
zadań.
Uwaga: Plik identyfikator_przyklad.txt zawiera przykładowe dane (20 wierszy).
Odpowiedzi dla danych z tego pliku są podane pod treściami zadań.
'''

'''
Podaj identyfikatory (seria+numer) tych dokumentów z pliku identyfikator.txt,
których suma cyfr z numerycznej części jest największa. Odpowiedź zapisz w pliku
wyniki4_1.txt, po jednym identyfikatorze w wierszu, w kolejności zgodnej z kolejnością
w pliku identyfikator.txt.
W pliku identyfikator_przyklad.txt jest jeden taki identyfikator. Prawidłowa
odpowiedź dla pliku identyfikator_przyklad.txt:
CHY728985 
'''

#Odczytujemy z pliku i zapisujemy jako liste stringow
wiersze = []
with open("DANE/identyfikator.txt") as f:
    for s in f.readlines():
        #dodaje zestripowane zeby nie bylo entera na koncu
        wiersze.append(s.strip())

#Znajdujemy najwieksza sume
maxSuma = 0
for w in wiersze:
    #Pierwsze 3 znaki jako seria
    seria = w[0:3]
    #Reszta jako numer
    numer = w[3:]
    suma = 0
    for cyfra in numer:
        suma += int(cyfra)
    if suma > maxSuma:
        maxSuma = suma


#Przechodzimy jeszcze raz i wypisujemy te ktorych suma jest rowne najwiekszej
for w in wiersze:
    #Pierwsze 3 znaki jako seria
    seria = w[0:3]
    #Reszta jako numer
    numer = w[3:]
    suma = 0
    for cyfra in numer:
        suma += int(cyfra)
    if suma == maxSuma:
        print(w,suma)
