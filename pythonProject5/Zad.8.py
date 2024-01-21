import math
def pole(a,b,kąt):
#a
    if kąt>=90:
        print("Trójkąt nie jest ostrokątny.")
        return None
#b
    elif (a<=0 or b<=0 or kąt >=180):
        print("Z podanych danych nie powstanie trójkąt.")
        return None
    else:
        wynikPole=0.5*a*b*math.sin(kąt)
        return wynikPole

a=float(input("Podaj długość boku a(cm): "))
b=float(input("Podaj długość boku b(cm): "))
kąt=int(input("Podaj szerokość kąta ostrego między nimi(w stopniach): "))

wynikPole=pole(a,b,kąt)
print(wynikPole)