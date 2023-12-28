def powtorka(i):
    nCiag=""
    for znak1 in i:
        if i.count(znak1) > 1:
            nCiag +='@'
        else:
            nCiag += znak1
    return nCiag

ciagZnakow=input("Podaj ciąg znaków: ")
ciag2=powtorka(ciagZnakow)
print("Zmieniony ciąg znaków to: ", ciag2)