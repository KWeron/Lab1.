def imie(x):
    ostatniaLitera=x[-1]
    if ostatniaLitera=="a":
        return "jest to kobieta"
    else:
        return "jest to mężczyzna"
x=str(input("Podaj imię: "))
print(imie(x))