import http.client
import json
import pandas as pd

def obter_ceps(cep):
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


ceps_ex = ["01001000", "29114035", "35010-230", "05891160"]
for cep in ceps_ex:
    endereco = obter_ceps(cep)

    salvar_endereco(endereco)

    print(endereco)
