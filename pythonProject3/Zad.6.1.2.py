#wykorzystujące continue
while True:
    x = input("Podaj daną: ")
    if x.isdigit():
        x=int(x)
        if x>0:
            print("to jest liczba")
            continue
    else:
        print("To nie jest liczba całkowita.")
        break