'''
Podaj, ile wynosi najmniejsza liczba wierszy, które należy usunąć, żeby obraz miał pionową oś
symetrii. Obraz ma pionową oś symetrii, jeśli w każdym wierszu i-ty piksel od lewej strony
przyjmuje tę samą wartość, co i-ty piksel od prawej strony, dla dowolnego 1 ≤ i ≤ 320.
Dla danych z pliku przyklad.txt wynikiem jest 3.
'''

wiersze = []
with open("Dane_PR2/przyklad.txt") as f:
    for s in f.readlines():
        wiersze.append(s.strip())

cnt = 0
for w in wiersze:
    listaWiersza = w.split()
    # print("kajjak"[0:3],"".join(list(reversed("kajjak"[3:6]))))
    # if listaWiersza[0:160] == list(reversed(listaWiersza[160:320])):
    #     cnt += 1
    jestSymetryczny = True
    for i in range(0,320):
        if listaWiersza[i] != listaWiersza[320-i-1]:
            jestSymetryczny = False
    if not jestSymetryczny:
        cnt += 1

print(cnt)
