def ukladanie(a, b):
    lista = []
    if a >= b:
        while a >= b:
            lista.append(a)
            a -= 1
    else:
        while b >= a:
            lista.append(b)
            b -= 1
    return lista

proba = ukladanie(-3, 5)
print(proba)
