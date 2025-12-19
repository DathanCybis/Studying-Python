class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = None
        self.set_preco(preco)


    def get_preco(self):
        return self._preco
    

    def set_preco(self, valor):
        if valor >= 0:
            self._preco = valor
        else:
            print("O preço não pode ser negativo")


    def aplicar_desconto(self, desconto_porcentual):
        novo_preco = self._preco * (1 - desconto_porcentual / 100)
        self.set_preco(novo_preco)


p1 = Produto("Camiseta", 50)

print(f"Preço atual de {p1.nome}: R${p1.get_preco()}") # Preço atual de Camiseta: R$50

