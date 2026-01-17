import http.client
import json

def obter_dados(cnpj):
    conexao = http.client.HTTPSConnection('www.receitaws.com.br')

    conexao.request("GET", f"/v1/cnpj/cnpj")


cnpj_ex = "33157312000162"
