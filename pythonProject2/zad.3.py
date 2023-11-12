a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
c = float(input("Podaj wartość c: "))

#a*x**2+b*x+c=0

delta=(b**2)-(4*a*c)
print("Delta równa: ",delta)
if a!=0:
    if delta < 0:
        print("Równanie nie ma rozwiązania")
    elif delta == 0:
        x = -b / (2 * a)
        print("Równanie ma jedno rozwiązanie: ", x)
    else:
        x1 = (-b - delta**(1 / 2)) / (2 * a)
        x2 = (-b + delta**(1 / 2)) / (2 * a)
        print("Równanie ma dwa rozwiązania: ", x1, x2)
else:
    x=-c/b
    print("Równanie nie jest kwadratowe i ma jedno rozwiązanie: ", x)
