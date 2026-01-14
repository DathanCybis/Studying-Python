import http.client

import json

import pandas as pd

def obter_cep(cep):
    conexao = http.client.HTTPSConnection("viacep.com.br")

    conexao.request("GET", f"/ws/{cep}/json/")

    resposta = conexao.getresponse()

    dados = resposta.read()

    endereco = json.loads(dados.decode("utf-8"))

    return endereco


def salvar_endereco(endereco, nome_arquivo="endereco.xlsx"):
    if "erro" not in endereco:
        df = pd.DataFrame([endereco])

        df.to_excel(nome_arquivo, index=False)

        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}")

    else:
        print("Não foi possível salvar os dados: CEP não encontrado.")


cep_ex = "01001000"

endereco = obter_cep(cep_ex)

salvar_endereco(endereco)

print(endereco)
