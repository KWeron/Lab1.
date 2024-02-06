import random

# Funkcja do generowania listy liczb losowych
def generuj_liste(rozmiar):
    return [random.randint(1, 100) for _ in range(rozmiar)]

# Funkcja do obliczania iloczynu elementów podzielnych przez 7
def oblicz_iloczyn(lista):
    iloczyn = 1
    for liczba in lista:
        if liczba % 7 == 0:
            iloczyn *= liczba
    return iloczyn

# Ustaw rozmiar listy
rozmiar_listy = 10

# Wygeneruj listę liczb losowych
lista_liczb = generuj_liste(rozmiar_listy)

# Wyświetl wygenerowaną listę
print("Wygenerowana lista liczb:", lista_liczb)

# Oblicz iloczyn elementów podzielnych przez 7
iloczyn_podzielnych_przez_7 = oblicz_iloczyn(lista_liczb)

# Wyświetl wynik
print("Iloczyn elementów podzielnych przez 7:", iloczyn_podzielnych_przez_7)
