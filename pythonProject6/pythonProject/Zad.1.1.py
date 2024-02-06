#fukcja aby obliczyć sumę od a do b
def koncowaSuma(a,b):
    suma=0
    while a<=b:
        suma +=a
        a += 1
    return suma

#pobieranie danych od użytkownika
a = int(input("Podaj mniejszą liczbę a:"))
b = int(input("Podaj większą liczbę b:"))

#wywołanie funkcji i sprawdzenie warunku
wynik=koncowaSuma(a,b)

if a>b:
    print("Błędnie podane wartości")
else:
    print("Końcowy wynik to:", wynik)
