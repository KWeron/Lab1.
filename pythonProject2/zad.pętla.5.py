import random

n=int(input("Liczba studentów: "))
x=1
s=0
#x-student 1
#x+1-student 2
#o-liczba punktów studenta
#ś-średnia liczba punktów
#s-suma

while x <= n:
    o = (random.randint(1, 40))
    s += o
    print("Liczba punktów studenta:",x,"wynosi: ",o)
    x += 1

ś=s/n
print("Średnia liczba punktów w grupie wynosi: ",ś)