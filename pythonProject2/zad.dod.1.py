l=input("Wprowadź literę: ")

if l.isalpha():
    if l.islower():
        print(f"Wprowadzona litera {l} jest małą literą")
    else:
        print(f"Wprowadzona litera {l} jest dużą literą")
else:
    print("Nie jest to litera")