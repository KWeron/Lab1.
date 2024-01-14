def palindrowoe(slowo):
    if slowo==slowo[::-1]:
        return "Podane słowo jest palindromem."
    else:
        return "Podane słowo nie jest palindromem."
slowo=str(input("Podaj słowo: "))
print(palindrowoe(slowo))