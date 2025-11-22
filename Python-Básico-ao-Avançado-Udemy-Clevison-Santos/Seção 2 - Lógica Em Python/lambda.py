# Funções anônimas (lambda)

# -> Função Regular:
def dobrar(n):
    return n * 2

print("Função Regular:", dobrar(5)) # Saída: 10


# -> Função Lambda
dobrar_com_lambda = lambda n: n * 2

print("Função Lambda:", dobrar_com_lambda(5)) # Saída: 10
