#Jesli korzystamy z funkcji z biblioteki math musimy zaimportowac
import math

'''Zamiana typow danych'''

#Napis na liczbe
s = "123"
n = int(s)
print(n)

#Liczbe na napis
n = 123
s = str(123)
print(s)


'''
Silnia (n!)
'''
#Liczy silnie z 5
silnia = math.factorial(5)
print(silnia)

'''
Wartosc bezwzgledna (|x|)
'''
#Wartosc bezwzgledna z -100
bzwg = abs(-100)

'''
NWD - najwiekszy wspolny dzielnik z dwoch liczb
'''
nwd = math.gcd(21,35)

'''
NWD - najwiekszy wspolny dzielnik z listy liczb
'''
#Definicja wrzucacie tylko na gore programu
def nwdZListy(l):
    if len(l) == 0:
        print("PUSTA LISTA!")
    else:
        nwd = l[0]
        for i in l:
            nwd = math.gcd(nwd,i)
        return nwd

#Uzycie
print(nwdZListy([35,21,14,70]))
l = [500,145,35,80]
print(nwdZListy(l))

'''
Zaokrąglanie
'''

i = 10.534
#Zaokrąglic do dwoch miejsc po przecinku
zaok = round(i,2)
print(zaok)

#Zaokraglanie w dol
zaok = math.floor(i)
print(zaok)

#Zaokraglanie w gore
zaok = math.ceil(i)
print(zaok)

def sumaElementowListy(l):
    #Suma elementów listy
    suma = 0
    for i in l:
        #zwieksz sume o i zamienione na liczbe
        suma += int(i)
    return suma

'''
Sprawdza czy wszystkie elementy z l1 zawieraja sie w l2
'''
def zawieraElementy(l1,l2):
    znajdujaSie = True
    for i in l1:
        #Jesli znajdziemy taki ktory sie nie znajduje to przestawiamy na false
        if i not in l2:
            znajdujaSie = False
    return znajdujaSie

#Uzycie
lista1 = [1,2,3]
lista2 = [5,6,7,8,9,1,2,6,4,3]
if zawieraElementy(lista1,lista2):
    print("Lista1 zawiera elementy listy2")


#Sprawdza czy liczba podana jest pierwsza
def czy_pierwsza(n):
    for i in range(2,(n//2)+1):
        if n % i == 0:
            return False
    return True

#Uzycie

print(czy_pierwsza(5))

print(czy_pierwsza(100))

if czy_pierwsza(2137):
    print("Papiesz")


