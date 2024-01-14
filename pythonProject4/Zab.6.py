def poleT(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return "Błędnie podana wartość."
    else:
        if a+b<=c or b+c<=a or a+c<=b:
            return "Z podanych boków nie da się utworzyć trójkąta."
        else:
            p=(a+b+c)/2
            pole=(p*(p-a)*(p-b)*(p-c))**0.5
            return "Pole trójkąta to: " + str(pole)

a=float(input("Podaj wartość a: "))
b=float(input("Podaj wartość b: "))
c=float(input("Podaj wartość c: "))
print(poleT(a,b,c))