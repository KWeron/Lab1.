i=str(input("Podaj imię: "))
print("Witaj "+i)

w=int(input("Podaj swój wiek: "))
print(f"Twój wiek to: ", w)

m=str(input("Podaj imię: "))
n=str(input("Podaj nazwisko: "))
initials=m[0].upper()+n[0].upper()
print("Twoje inicjały to: "+ initials)

tekst1="Latem jest ciepło. "
print((tekst1)*5)

tekst2="Zimą pada śnieg. "
tekst3="W jesieni spadają liście. "
tekst4=tekst2+tekst3
print(tekst2+tekst3+"\n"+tekst4)

tekst5="Wiosną zaczyna rozkwitać życie. "
tekst6="Latem jest ciepło. "
tekst7=tekst5[:len(tekst5)//2]+tekst6[len(tekst6)//2:]
print(tekst5+tekst6+'\n'+tekst7)