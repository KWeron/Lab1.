x = int(input("Podaj ilość linii i gwiazdek:"))
star='*'
space=' '
i=x

for n in range(0, x+1):
    print(i *space + n * star)
    i-=1
