a=float(input("Podaj pierwszą liczbę: "))
b=float(input("Podaj drugą liczbę: "))

# p-liczba pierwsza
# k-liczba końcowa

if a>b:
    p=b
    k=a
elif b>a:
    p=a
    k=b
else:
    print("Podane liczby są równe sobie")

if a!=b:
    while p<=k:
        p += 1
        if p%2==0:
            print(p)
        else:
            continue
    else:
        print("KONIEC")