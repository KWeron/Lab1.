import keyword

f=keyword.iskeyword("for")
print("Słowo 'for' jest słowem kluczowym?: ", f)

p=keyword.iskeyword("print")
print("Słowo 'print' jest słowem kluczowym?: ", p)

b=keyword.iskeyword("break")
print("Słowo 'break' jest słowem kluczowym?: ", b)

d=keyword.iskeyword("done")
print("Słowo 'done' jest słowem kluczowym?: ", d)

ba=keyword.iskeyword("bad")
print("Słowo 'bad' jest słowem kluczowym?: ", ba)

#2 sposób
slowa=["for", "print", "break", "done", "bad"]
for sprawdz in slowa:
    print("Słowo", sprawdz,"jest słowem kluczowym?: ", keyword.iskeyword(sprawdz))
