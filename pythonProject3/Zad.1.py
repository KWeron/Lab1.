print("Za pomocą pętli for wpisz na ekranie ciąg liczb: ")
print("1- 1,2,3,...,99,100")
print("2- 100,99,...,2,1,0")
print("3- 7,14,21,...,70,77")
print("4- 20,18,...,2,0")
x = int(input("Podaj numer podpunktu: "))

if x == 1:
    for i in range(1, 101):
        print(i)

elif x == 2:
    for b in range(100, -1, -1):
        print(b)
elif x == 3:
    for c in range(7, 78, 7):
        print(c)
elif x == 4:
    for z in range(20, -1, -2):
        print(z)
else:
    print("Błędnie wprowadzona liczba")