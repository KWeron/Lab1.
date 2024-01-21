import random

rozpoczeciePrzedzialu=float(input("Podaj początek pzedziału: "))
koniecPrzedzialu=float(input("Podaj koniec przedziału: "))
limitElementow = 10
krotka=()

if rozpoczeciePrzedzialu >= koniecPrzedzialu:
    print("Początek przedzału musi być mniejszy niż koniec.")
else:
    for i in range(limitElementow):
        losowy=random.randint(rozpoczeciePrzedzialu, koniecPrzedzialu)
        krotka+= (losowy, )
print(krotka)

mnozenieKrotki=1
for wynik in krotka:
    mnozenieKrotki *= wynik

sredniaGeometryczna=(mnozenieKrotki**(1/limitElementow))
print("Średnia geometyczna danej krotki to: ", sredniaGeometryczna)