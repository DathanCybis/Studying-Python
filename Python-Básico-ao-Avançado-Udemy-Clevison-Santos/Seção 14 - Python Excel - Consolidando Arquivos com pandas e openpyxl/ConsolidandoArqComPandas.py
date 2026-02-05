import pandas as pd
import os

caminhoArquivos = "C:\\...\\ArquivosExcel"

listaArquivos = os.listdir(caminhoArquivos)

print(listaArquivos)

listaCaminhoEArquivo = [caminhoArquivos + '\\' + arquivo for arquivo in listaArquivos if arquivo[-4:] == "xlsx"]

print("-------------###--------------###-----------")
print("-------------###--------------###-----------")
print("-------------###--------------###-----------")
print(listaCaminhoEArquivo)
