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
obter_cotacao_dolar()
obter_cotacao_euro()
