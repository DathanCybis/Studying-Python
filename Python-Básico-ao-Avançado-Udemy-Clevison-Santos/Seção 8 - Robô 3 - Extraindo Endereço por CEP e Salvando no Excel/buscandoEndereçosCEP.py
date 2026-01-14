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


cep_ex = "01001000"

endereco = obter_cep(cep_ex)

print(endereco)
