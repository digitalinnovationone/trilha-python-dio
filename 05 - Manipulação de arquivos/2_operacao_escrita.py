arquivo = open(
    "/home/guilherme/Projetos/dio/codigo-fonte/trilha-python-dio/05 - Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()
