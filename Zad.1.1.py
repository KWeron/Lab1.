def koncowaSuma(a,b):
    suma=0
    while a<=b:
        suma +=a
        a += 1
    return suma

a = int(input("Podaj mniejszą liczbę a:"))
b = int(input("Podaj większą liczbę b:"))
wynik=koncowaSuma(a,b)

if a>b:
    print("Błędnie podane wartości")
else:
    print("Końcowy wynik to:", wynik)


