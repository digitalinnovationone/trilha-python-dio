arquivo = open(
    "/Python/trilha-python-dio/05 - Manipulação de arquivos//teste.txt", "w"
)
arquivo.writelines(["-"*36, "\n"])
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "-"*36, "\n"])

arquivo.writelines(["\n", "escrevendo novamente", "\n", "um", "\n", "novo", "\n", "texto simples", "\n"])
arquivo.writelines(["\n", "-"*36, "\n"])
arquivo.close()
