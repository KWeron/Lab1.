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
        if p%2==0:
            print(p)
            p += 1
        else:
            p += 1
            continue
    else:
        print("KONIEC")