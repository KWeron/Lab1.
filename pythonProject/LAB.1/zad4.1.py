import random
a= (random.randint(1, 100000))
print(a)
b=float(input("Podaj średnie spalanie na 100km [l]: "))

# x - przewidywanie zużycie paliwa
# y -szacowany koszt paliwa [6.5zł/l]

x=(a*b)/100
y=x*6.5
print("Przewidywanie zużycie paliwa wyniesie " + str(float(x)) + " l" + " oraz szacowany koszt paliwa wyniesie " + str(float(y)) + " zł")

