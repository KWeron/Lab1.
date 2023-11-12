print("Jaką operację chcesz tykonać?")
print("1-dodawanie")
print("2-odejmowanie")
print("3-mnożenie")
print("4-dzielenie")
print("5-potęgowanie")

x=int(input("Wpisz litere akcji od 1 do 5: "))

a = float(input("Podaj wartość a: "))
b = float(input("Podaj wartość b: "))
# d-wynik z dodawania
# o-wynik z odejmownaia
# m-wynik z mnożenia
# l-wynik z dzielenia
# p-wynik z potęgowania

# dodawanie
if x==1:
    d = a + b
    print(f"Wynik z dodwania wynosi: {float(d)}")
# odejmowanie
if x==2:
    o1 = a - b
    print(f"Wynik z odejmowania a-b wynosi: {float(o1)}")
    o2 = b - a
    print(f"Wynik z odejmownia b-a wynosi: {float(o2)}")
# mnożenie
if x==3:
    m = a * b
    print(f"Wynik z mnożenia wynosi: {float(m)}")

# dzielenie
if x==4:
    if b == 0:
        print("Dzielenie a/b nie ma rozwiązania")
    else:
        l2 = a / b
        print(f"Wynik z dzielenia a/b wynosi: {float(l2)}")

    if a == 0:
        print("Dzielenie b/a nie ma rozwiązania")
    else:
        l1 = b / a
        print(f"Wynik z dzielenia b/a wyniosi: {float(l1)}")
#potęgowanie
if x==5:
    p1=a**b
    print(f"Wynik z potęgowania a do b wynosi: {float(p1)}")
    p2=b**a
    print(f"Wynik potęgowania b do a wynosi: {float(p2)}")