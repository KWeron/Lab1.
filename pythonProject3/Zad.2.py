x = int(input("Podaj ilość gwiazdek w linii i w kolumnie:"))

for linia in range(x):
    for i in range(x):
        print("* ", end='')
    print("\n")