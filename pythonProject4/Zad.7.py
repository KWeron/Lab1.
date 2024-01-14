def odwrot(x):
    tyl=x[::-1]
    return tyl

x=str(input("Podaj słowo: "))
print("Podane słowo od tyu brzmi: ", odwrot(x))