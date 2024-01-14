def plec(x):
    ostatniaLitera=x[-1]
    if ostatniaLitera=="a":
        return "jest to kobieta"
    else:
        return "jest to mężczyzna"
x=str(input("Podaj imię: "))
print(plec(x))

imiona=["Karolina", "Oskar", "Maksymilian", "Oliwia", "Iwona"]
pary={imie: plec(imie) for imie in imiona}
print(pary)