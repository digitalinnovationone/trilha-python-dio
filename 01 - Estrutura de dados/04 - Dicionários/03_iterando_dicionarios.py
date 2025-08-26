contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print("=" * 70)
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 70)
# Iterando sobre as chaves e valores do dicionário

for chave, valor in contatos.items():
    print(chave, valor)
print("=" * 70)