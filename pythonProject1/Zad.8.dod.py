import string
def podlisty(lista, n):
    podlisty=[lista[i:i+n] for i in range(0, len(lista), n)]
    return podlisty

alfabet = list(string.ascii_lowercase)
n=int(input("Co ile podzielić liste na podlisy: "))
koniec=podlisty(alfabet,n)
print(koniec)