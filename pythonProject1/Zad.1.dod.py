import string

x = str(input("Wpisz zdanie: "))
y = x.lower()
bezSpacji = y.replace(" ", "")
uporzadkowanie = sorted(bezSpacji)
print("Te litery występują w tym zdaniu: ",uporzadkowanie)

alfabet = set(string.ascii_lowercase + "ąćęłńóśźż")
brakujaceLitery = alfabet - set(uporzadkowanie)
print("Tych liter z alfabtu nie zawiera to zdanie: ", sorted(brakujaceLitery))


