nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")
print(f'{texto.strip().upper()}.')


menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))
