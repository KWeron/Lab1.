#w1-wynik do przykładu a)
#w2-wynik do b)
#w3-wynik do c)

def A(x):
    if x>0:
        w1=2*x
    elif x==0:
        w1=0
    else:
        w1=-3*x
    return w1

def B(x):
    if x>=1:
        w2=x**2
    else:
        w2=x
    return w2

def C(x):
    if x>2:
        w3=2+x
    elif x==2:
        w3=8
    else:
        w3=x-4
    return w3

x=float(input("Podaj wartość x: "))

w1=A(x)
print(f"Wartość funkcji dla a(x) wyniesie {w1}")
w2=B(x)
print(f"Wartość funkcji dla b(x) wyniesie {w2}")
w3=C(x)
print(f"Wartość funkcji dla c(x) wyniesie {w3}")
