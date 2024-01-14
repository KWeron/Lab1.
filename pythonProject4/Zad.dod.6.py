def NWD(pierwszaLiczba, drugaLiczba):
    while drugaLiczba !=0:
        x=drugaLiczba
        drugaLiczba=pierwszaLiczba % drugaLiczba
        pierwszaLiczba=x
    return pierwszaLiczba

pierwszaLiczba=int(input("Podaj pierwszą liczbę: "))
drugaLiczba=int(input("Podaj drugą liczbę: "))
print(NWD(pierwszaLiczba, drugaLiczba))