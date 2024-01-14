def fun():
    x=float(input("Podaj liczbę x: "))
    if x>0:
        print("Podana liczba jest dodatnia.")
    elif x<0:
        print("Podana liczba jes ujemna.")
    else:
        print("Podana liczba ma wartość 0.")
    return x
print(fun())