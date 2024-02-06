def policz_rozne_znaki(tekst):
    unikalne_znaki = set(tekst)
    licznik_roznych_znaki = 0

    for znak in unikalne_znaki:
        if znak != 'a' and znak != 'b':
            licznik_roznych_znaki += tekst.count(znak)

    return licznik_roznych_znaki

# Przykład użycia:
ciag_znakow = input("Podaj ciąg znaków: ")
wynik = policz_rozne_znaki(ciag_znakow)
print(f"Ilość znaków różnych od 'a' i 'b' w podanym ciągu: {wynik}")
