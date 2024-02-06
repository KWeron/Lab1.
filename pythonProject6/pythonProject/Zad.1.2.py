def oblicz_S(N):
    suma = 0

    # Sprawdzamy, czy N jest dodatnie
    if N > 0:
        # Obliczamy sumę 1 + 2 + ... + N
        for i in range(1, N + 1):
            suma += i

        # Obliczamy wartość S
        S = suma / N

        # Zwracamy wynik
        return S
    else:
        # Jeżeli N nie jest dodatnie, informujemy użytkownika i zwracamy None
        print("Podano niepoprawną wartość N. N musi być większe od 0.")
        return None


# Pobieramy od użytkownika wartość N
N = int(input("Podaj wartość N: "))

# Wywołujemy funkcję i wyświetlamy wynik, jeśli N jest dodatnie
wynik = oblicz_S(N)
if wynik is not None:
    print(f"Wartość S dla N = {N} wynosi: {wynik}")