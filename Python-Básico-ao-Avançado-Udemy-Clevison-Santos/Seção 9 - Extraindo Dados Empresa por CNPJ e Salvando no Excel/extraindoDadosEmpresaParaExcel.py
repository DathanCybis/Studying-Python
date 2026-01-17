import http.client
import json

def obter_dados(cnpj):
    conexao = http.client.HTTPSConnection('www.receitaws.com.br')

    conexao.request("GET", f"/v1/cnpj/{cnpj}")

    resposta = conexao.getresponse()

    dados = resposta.read

    empresa = json.loads(dados.decode("utf-8"))

    conexao.close()

    if empresa.get('status', '' == 'ERROR'):
        return empresa.get('message', "Erro desconhecido")
    
    else:
        return empresa

cnpj_ex = "33157312000162"

dados_empresa = obter_dados(cnpj_ex)
