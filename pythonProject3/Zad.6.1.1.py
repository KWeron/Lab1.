#niewykorzystujące continue
x=input("Wprowadź daną: ")

if x.isdigit():
    x=int(x)
    if x>0:
        print("to jest liczba")
    else:
        print("Koniec")
else:
    print("To nie jest liczba całkowita.")