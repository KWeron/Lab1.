def przeformatZdanie(zdanie1):
    slowo = zdanie1.split()
    zdanie2 = ""

    for i in slowo:
        zdanie2 += i.capitalize()+i[-1].upper()+" "
    zdanie2=zdanie2.rstrip()
    return zdanie2
zdanie = str(input("Wprowadź zdanie: "))
zdanie2=przeformatZdanie(zdanie)
print("Przekształcone zdanie:", zdanie2)
