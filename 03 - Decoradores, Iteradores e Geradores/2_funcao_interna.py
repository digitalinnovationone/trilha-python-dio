def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna()
    funcao_2()


principal()
