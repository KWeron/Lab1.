import random
import string
def lista1(n, x):
    lista = []
    for _ in range(n):
        dlugoscCiaguLiter = random.randint(1, x)
        ciagLiter = ''.join(random.choice(string.ascii_lowercase) for _ in range(dlugoscCiaguLiter))
        lista.append(ciagLiter)
    return lista

n = int(input("Podaj wartość n: "))
x = int(input("Podaj wartość x: "))
utworzonaLista = lista1(n, x)

print(utworzonaLista)

krotka=tuple(utworzonaLista)
print(krotka)

#a
def ilosc(lista):
    ilZnakow = sum(len(znaki) for znaki in lista)
    return ilZnakow

print("Ilość znaków w liście wynośi: ", ilosc(utworzonaLista))

#b
def iloscK(lista):
    iloscK1=sum(znaki.count('k') for znaki in lista)
    return iloscK1

print("W tej liście 'k' występuje tyle razy: ", iloscK(utworzonaLista))

#c
def iloscKT(lista):
    iloscKT1=sum(znaki.count('kt') for znaki in lista)
    return iloscKT1

print("W tej liście 'kt' występuje tyle razy: ", iloscKT(utworzonaLista))

#d
s = int(input("Podaj wartość s: "))
def dluzszeOdS(lista, s):
     dluzsze = dluzszeOdS(utworzonaLista, s)

s=int(input("Podaj wartość s: "))
print