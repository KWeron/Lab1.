import random
def poczatek():
    x=int(input("Podaj początek przedziału liczbowego: "))
    y=int(input("Podaj koniec przedziału liczbowego: "))
    if x>y:
        x, y = y, x
    if x==y:
        print("Podano dwie takie same liczby.")
    else:
        zgadywanaLiczba = random.randint(x, y)


    iloscProb=3
    for i in range(iloscProb):
        try:
            uzytkownik = int(input("Co to może być za liczba? "))
            if uzytkownik==zgadywanaLiczba:
                print("Udało się!")
            elif (uzytkownik>zgadywanaLiczba):
                print("za dużo")
            else:
                print("za mało")
        except ValueError:
            print("Nie podałeś liczb")
    print("Nie udało się :(")
