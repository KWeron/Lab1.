import random

# Tworzenie pierwszej listy z liczbami losowymi
lista_liczb = [random.randint(1, 100) for _ in range(10)]

print("Pierwsza lista:", lista_liczb)

# Tworzenie drugiej listy zawierającej tylko liczby parzyste
lista_parzystych = [liczba for liczba in lista_liczb if liczba % 2 == 0]

print("Druga lista (liczby parzyste):", lista_parzystych)
