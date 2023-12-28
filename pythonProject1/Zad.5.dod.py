def dlugieSlowo(zdanie):
    wszystkieSlowa = zdanie.split()
    longSlowo = max(wszystkieSlowa, key=len)
    dlugoscSlowa = len(longSlowo)
    return longSlowo,dlugoscSlowa

zdanie = str(input("Wprowadź zdanie: "))

longSlowo,dlugoscSlowa = dlugieSlowo(zdanie)
print("Najdłuższe zdanie to:", longSlowo,", którego długość to:", dlugoscSlowa,"liter.")