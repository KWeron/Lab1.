a=float(input("Podaj wartość a: "))
b=float(input("Podaj wartość b: "))
#0=a*x+b

if a==0:
    print("Równanie nie ma rozwiązania")
else:
    x=-b/a
    print(f"Wartość x wyniesie {float(x)}")
