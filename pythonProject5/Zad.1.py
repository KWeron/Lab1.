import random
#a)
szczesliwy=random.randint(1,15)
print("Szęściwy numere to: ", szczesliwy)
#b)
tab = [2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997]
szczesliwyRocznik=random.choice(tab)
print("Szczęśliwy rocznik to: ", szczesliwyRocznik)
#c
lotek=list(range(1,50))
szescKul=random.sample(lotek, 6)
print("Wylosowano 6 następujących kul: ", szescKul)