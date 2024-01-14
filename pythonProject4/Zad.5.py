def fun(wzrost, masa):
    BMI=masa/(wzrost**2)
    if BMI<18.5:
        print("Niedowaga")
    elif 18.5<=BMI<=24.9:
        print("Pożądana masa ciała")
    elif 25<=BMI<=29.9:
        print("Nadwaga")
    else:
        print("Otyłość")
    return BMI

wzrost = float(input("Podaj wzrost [metry]: "))
masa = float(input("Podaj masę ciała [kilogramy]: "))
print(fun(wzrost, masa))