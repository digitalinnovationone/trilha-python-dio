def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


def exibir_informacoes_carro(modelo, marca, /, ano, *, placa):
    print(f"""
Marca: {marca}
Modelo: {modelo}
Ano: {ano}
Placa: {placa}
""")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(
    **{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}
    )

# É obrigatorio passar a placa como argumento nomeado
exibir_informacoes_carro("Fiat", "Palio", 1999, placa="DEF-789")
