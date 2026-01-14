# Importa a biblioteca necessária
import requests
# Forma atualizada de usar
# Função para obter a cotação do dólar usando a API AwesomeAPI
def obter_cotacao_dolar():
    # URL da API para dólar em relação ao real
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
 
    try:
        # Envia uma requisição GET para a API
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na resposta
 
        # Converte o conteúdo da resposta para JSON
        dados = resposta.json()
 
        # Extrai o valor da cotação de compra (bid)
        cotacao = dados['USDBRL']['bid']
 
        # Exibe a cotação
        print(f"Cotação atual do dólar: R$ {cotacao}")
        return cotacao
 
    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except Exception as erro:
        print("Erro ao processar os dados:", erro)

# Função para obter a cotação do euro usando a API AwesomeAPI
def obter_cotacao_euro():
    # URL da API para euro em relação ao real
    url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
 
    try:
        # Envia uma requisição GET para a API
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na resposta
 
        # Converte o conteúdo da resposta para JSON
        dados = resposta.json()
 
        # Extrai o valor da cotação de compra (bid)
        cotacao = dados['EURBRL']['bid']
 
        # Exibe a cotação
        print(f"Cotação atual do euro: R$ {cotacao}")
        return cotacao
 
    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)
    except Exception as erro:
        print("Erro ao processar os dados:", erro)

# Chamada da função
valorDolar = obter_cotacao_dolar()
valorEuro = obter_cotacao_euro()

import os
import xlsxwriter

# Caminho onde o arquivo será salvo (pasta atual)
caminhoArquivo = os.path.join(os.getcwd(), "dados.xlsx")

# Cria o arquivo Excel
workbook = xlsxwriter.Workbook(caminho)

# Cria uma planilha
worksheet = workbook.add_worksheet("Planilha1")

# Escrevendo os dados
worksheet.write("A1", "Dolar")
worksheet.write("B1", "Euro")

valorDolar = float(valorDolar)
valorEuro = float(valorEuro)

worksheet.write("A2", valorDolar)
worksheet.write("B2", valorEuro)

# Fecha o arquivo (muito importante)
workbook.close()

print("Planilha criada com sucesso!")

os.startfile(caminho)
