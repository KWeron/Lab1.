def ileZnakow(slowo):
    iloscWielkich=0
    iloscMalych=0
    inneZnaki=0

    for litera in slowo:
        if litera.isupper():
            iloscWielkich +=1
        elif litera.islower():
            iloscMalych +=1
        else:
            inneZnaki +=1

    wynik={'Ilość dużych liter': iloscWielkich,'Ilość małych liter': iloscMalych, 'Ilość pozostałych znaków': inneZnaki}
    return wynik

slowo=input("Wprowadz zdanie/zdanie z innymi znakami: ")
print(ileZnakow(slowo))