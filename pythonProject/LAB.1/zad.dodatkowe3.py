a=float(input("Podaj wartość a: "))
b=float(input("Podaj wartość b: "))
# d-wynik z dodawania
# o-wynik z odejmownaia
# l-wynik z dzielenia

#dodawanie
d=a+b
print(f"Wynik z dodwania wynosi: {float(d)}")
#odejmowanie
o1=a-b
print(f"Wynik z odejmowania a-b wynosi: {float(o1)}")
o2=b-a
print(f"Wynik z odejmownia b-a wynosi: {float(o2)}")
#dzielenie
if b==0:
    print("Dzielenie a/b nie ma rozwiązania")
else:
    l2=a/b
    print(f"Wynik z dzielenia a/b wynosi: {float(l2)}")

if a==0:
    print("Dzielenie b/a nie ma rozwiązania")
else:
    l1=b/a
    print(f"Wynik z dzielenia b/a wyniosi: {float(l1)}")
