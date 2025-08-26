contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
print(copia)

copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
