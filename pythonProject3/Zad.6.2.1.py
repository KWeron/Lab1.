#niewykorzystujące continue
x=input("Wprowadź daną: ")

if x.isdigit():
    x=int(x)
    if x>0:
        wynik=x**1/2
        print(f"Pierwiastek kwadratowy z",x , "wynosi: ", wynik)
    else:
        print("Dziękujemy za skorzystanie z naszej aplikacji.")
else:
    print("To nie jest liczba całkowita.")