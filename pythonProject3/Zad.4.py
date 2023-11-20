n = int(input("Podaj numer wyrazu (liczba naturalna)(n): "))
a = float(input("Podaj wartość dla pierwszego ciągu arytmetycznegi (a): "))
r = float(input("Różnica ciągu arytmetycznego (r): "))

for i in range(n):
    x=a+(i)*r
    print(x)

