def exibir_infos(**kwargs):
    for chave, valor in kwargs.items():
        print(chave + ": " + str(valor))

exibir_infos(nome="João", idade=24, pais="Brasil")
