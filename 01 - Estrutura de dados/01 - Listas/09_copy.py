lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]


[n**2 if n > 6 else n for n in range(10) if n % 2 == 0]

print(n)  # NameError: name 'n' is not defined