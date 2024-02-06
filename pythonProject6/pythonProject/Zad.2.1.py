def sum_and_prepend(lst):
    # Sprawdź, czy lista nie jest pusta
    if not lst:
        print("Lista jest pusta.")
        return

    # Oblicz sumę elementów listy
    suma = sum(lst)

    # Wstaw sumę na początek listy
    lst.insert(0, suma)

    # Wydrukuj zaktualizowaną listę
    print("Zaktualizowana lista po dodaniu sumy na początku:", lst)

# Przykładowa lista
moja_lista = [1, 2, 3, 4, 5]

# Wywołaj funkcję sum_and_prepend z daną listą
sum_and_prepend(moja_lista)
