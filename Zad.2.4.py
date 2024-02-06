import random
x=int(input("Podaj liczbę x: "))

lista1=[random.randint(-x, x) for _ in range(5)]
lista2=[liczba > 0 for liczba in lista1]

print(lista1)
print(lista2)