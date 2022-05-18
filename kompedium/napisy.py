#Utworznie nowego stringa o wartosci 21345642
s = "21345642"

'''
Przechodzenie przez napis (znak po znaku)
'''

#Jesli chcemy cos zrobic z literami
s = "Abcdsdgdadag"
for c in s:
    print(c,end=" ")
print()
#Jesli chcemy cos zrobic z kazda cyfra osobno (zastosowac do obliczen)
s = "1234453264"
for c in s:
    cyfra = int(c)
    #Wypisuje kwadrat kazdej cyfry
    print(cyfra ** 2, end=" ")
print()

'''
 Zamiana wszystkich wystapien danego ciagu znakow na inny
'''
#Zamienia kazde a na *
s = "abcdabcdabcd"
s2 = s.replace("a","*")
print(s2)

#Zamienia kazdy ciag abc na df
s = "abcdabcdabcd"
s2 = s.replace("abc","df")
print(s2)



'''
Konwertowanie napisu na floata
'''

#gdy jest z kropką
s = "5.123"
f = float(s)
print(f)

#Gdy jest z przecinkiem
s = "5,123"
f = float(s.replace(",","."))
print(f)

'''
 Zawieranie sie ciagu znakow w jakims stringu
'''

s = "duuuupa"

#Zawiera ciag znakow
if "uup" in s:
    print("Zawiera ciag znakow uup")

#Nie zawiera ciagu znakow
if "dupa" not in s:
    print("Nie zawiera ciagu znakow dupa")

#Zawiera litere z
if "z" in s:
    print("Zawiera z")

#Zliczenie wystapien danego ciagu znakow
s = "abcdabcdadaggdag"
n = s.count("a")
print(n)


#Usuniecie bialych spacji z konca napisu
s = "adggddagadg\n"
s2 = s.strip()
print(s2)


'''
ASCII
'''

#Pzypisujemy do n kod znaku 'A' czyli liczbe 65
n = ord("A")

#Przypisujemy do znaku kod 65 jako znak czyli 'A'
znak = chr(65)

#Wypiszmy kody ascii dla kazdego znaku w stringu
s = "abcdefgh1234 "
for c in s:
    n = ord(c)
    print(c,n)


#Przesuniecie liter A-Z o jeden w 3 prawo
#czyli A staje sie D
#B staje E
#itd
#Z staje sie C
s = "ABCDEFGHZ"
for c in s:
    #Zamieniamy z kodu ascii 65,66,67 itd
    #na znormalizowana forme 0,1,2 itd
    n = (ord(c) - ord("A"))
    #Przesuwamy o 3 w prawo
    n += 3

    #Zawijamy przesuniecie do 26 czyli tyle ile jest liter w alfabecie  (27 staje sie 1, 28 staje sie 2 itd)
    n %= 26

    #Zamieniamy spowrotem (0,1,2, itd) na (65,66,67, itd)
    n += ord("A")

    #Robimy cos dalej z przesunietym znakiem
    przesunietyZnak = chr(n)

#Zliczeniec cyfr w stringu
s = "AB8CDR6EQRE4QA9HJGDU0"
cnt = 0
for c in s:
    if c.isdigit():
        cnt += 1
print(cnt)


#Sprawdzanie ilosci cyfr w calym liscie wierszy
wiersze = ["AB8CDR6EQRE4QA9HJGDU0",
           "AB8CDR6EQRE4QA9HJGDU0",
           "AB8CDR6EQREQA9HJGDU"]

cnt = 0
for w in wiersze:
    for c in w:
        if c.isdigit():
            cnt += 1
print(cnt)