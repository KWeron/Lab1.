import random
a = random.randint(3,7)
b = random.randint(3,7)

zbiorX = set(random.randint(0,10) for _ in range(a))
zbiorY = set(random.randint(0,10) for _ in range(b))
print("Zbiór X: ", zbiorX)
print("Zbiór Y: ", zbiorY)
#a
print("a) Czy w zbiorze X znajduje się liczba 5?: ",5 in zbiorX)

#b
print("b) Czy zbiór X jest podzbiorem zbioru Y?: ", zbiorX.issubset(zbiorY))

#c
print("c) Czy zbiór Y jest podzbiorem zbioru X?: ", zbiorY.issubset(zbiorX))

#d
print("d) Czy zbiór X jest nadzbiorem zbioru Y?: ", zbiorX.issuperset(zbiorY))

#e
print("e) Czy zbiór Y jest nadzbiorem zbioru X?: ", zbiorY.issuperset(zbiorX))

#f
print("f) Suma zbioru X i Y to: ", zbiorX.union(zbiorY))

#g
print("g) Różnica zbiorów X oraz Y to: ", zbiorX.difference(zbiorY))

#h
print("h) Różnica zbiorów Y oraz X to: ", zbiorY.difference(zbiorX))

#i
print("i) Iloczyn zbiorów X oraz Y to: ", zbiorX.intersection(zbiorY))

#j
print("j) Różnica symetryczna zbiorów X oraz Y to: ", zbiorX.symmetric_difference(zbiorY))

#k
najwiekszyX = max(zbiorX)
print("k1) Wartość najwyższego elementu w zbiorze X to: ", najwiekszyX)

najwiekszyY = max(zbiorY)
print("k2) Wartość najwyższego elementu w zbiorze Y to: ", najwiekszyY)

#l
pierwszyEleX=zbiorX.pop()
zbiorY.add(pierwszyEleX)
print("l) Zbiór Y wygląda następujaco: ", zbiorY)

#m
print("m) Przekopiowane wszystkie elementy ze zbioru X do zbioru Y to: ", zbiorY.update(zbiorX))

#n
zbiorY.clear()
zbiorX.clear()
print(f"Zbiór X zawiera: {zbiorX}, natomiast zbiór Y zawiera: {zbiorY}")
