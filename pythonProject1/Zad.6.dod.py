def palin(slowo):
    odTylu=slowo[::-1]
    if slowo==odTylu:
        return True
    else:
        return False

podaSlowo=input("Podaj ciąg znaków: ")
if palin(podaSlowo):
    print("Słowo/Ciąg znaków jest palindromem")
else:
    print("To słowo/ciąg znaków nie jest palindromem")