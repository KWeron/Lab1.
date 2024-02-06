def sprawdz_warunek(a, b, c):
    if c*c + b*b == a*a:
        return 1
    else:
        return 0

# Przykładowe wywołanie funkcji
a = 5
b = 4
c = 3
wynik = sprawdz_warunek(a, b, c)

print("Wynik sprawdzenia warunku dla a =", a, ", b =", b, ", c =", c, "to:", wynik)
