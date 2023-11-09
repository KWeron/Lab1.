wiek=int(input("Podaj wiek: "))

if wiek<0:
    print("Błędznie podany wiek")
elif wiek <=4:
    print("Wejście bezpłatne")
elif wiek <=18:
    print("Koszt biletu 10zł")
else:
    print("Koszt biletu 20zł")