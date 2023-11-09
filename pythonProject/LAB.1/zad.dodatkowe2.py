
a=float(input("Podaj wartość boku a: "))
b=float(input("Podaj wartość boku b: "))
c=float(input("Podaj wartość boku c: "))

p=(a+b+c)/2
print(f"Wartość p: {float(p)}")

P=(p*(p-a)*(p-b)*(p-c))**(1/2)
print(f"Pole trójkąta wynosi {float(P)}")
