pessoa = {"nome": "Guilherme", "idade": 28}
# Declarando um dicionário
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
pessoa["endereco"] = "Rua A, 123"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234", "endereco": "Rua A, 123"}
pessoa["idade"] = 29  # Atualizando o valor da chave "idade"
print(pessoa)
