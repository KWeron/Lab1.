listaImion = ["Samanta", "Basia", "Marek", "Kamil"]

#a
posortowanaLImion = sorted(listaImion)
print(posortowanaLImion)

#b
posortowanaLImion.append("Eryk")
posortowanaLImion.append("Oliwia")
print(posortowanaLImion)
print(posortowanaLImion.pop())

#c
posortowanaLImion.insert(3, "Piotrek")
print(posortowanaLImion)

#d
posortowanaLImion.reverse()
print(posortowanaLImion)
duplikat=posortowanaLImion*2
duplikat.sort()
print(duplikat)

