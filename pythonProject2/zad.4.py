x = float(input("Podaj wartość x: "))
y = float(input("Podaj wartość y: "))
z = float(input("Podaj wartość z: "))

if x<y<z:
    print("Najmniejszą liczą jest: ",x,"następnie: ",y,",a największą jest: ",z )
elif x<z<y:
    print("Najmniejszą liczą jest: ", x, "następnie: ", z, ",a największą jest: ", y)
elif y<x<z:
    print("Najmniejszą liczą jest: ", y, "następnie: ", x, ",a największą jest: ", z)
elif y<z<x:
    print("Najmniejszą liczą jest: ", y, "następnie: ", z, ",a największą jest: ", x)
elif z<y<x:
    print("Najmniejszą liczą jest: ", z, "następnie: ", y, ",a największą jest: ", x)
elif z<x<y:
    print("Najmniejszą liczą jest: ", z, "następnie: ", x, ",a największą jest: ", y)
elif x==y<z:
    print("Liczba x i y są równe: ", x, ",a największą jest: ", z)
elif x==z<y:
    print("Liczba x i z są równe: ", x, ",a największą jest: ", y)
elif z==y<x:
    print("Liczba y i z są równe: ", y, ",a największą jest: ", x)
else:
    print("Wszystkie liczby są sobie równe.")