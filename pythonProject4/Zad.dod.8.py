def sprawdz(slowo1, slowo2):
    if sorted(slowo1)==sorted(slowo2):
        return "Podane słowa są anagramami"
    else:
        return "Podane słowa nie są anagramami"

slowo1=str(input("Podaj pierwsze słowo: "))
slowo2=str(input("Podaj drugie słowo: "))
print(sprawdz(slowo1,slowo2))