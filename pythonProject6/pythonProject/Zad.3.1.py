def generuj_liste(a, b, c):
    lista = [b + i * c for i in range(a)]
    return lista

# Przykładowe użycie funkcji
a = 5
b = 10
c = 2
wynik = generuj_liste(a, b, c)
print(wynik)
