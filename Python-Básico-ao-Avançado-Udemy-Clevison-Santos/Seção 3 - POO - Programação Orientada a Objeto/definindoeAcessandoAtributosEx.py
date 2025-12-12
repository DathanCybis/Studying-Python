class Fruta:
    def __init__(self, nome, preco_kg, estoque_kg):
        self.nome = nome
        self.preco_kg = preco_kg
        self.estoque_kg = estoque_kg

    def exibir(self):
        print(f"O preço da fruta {self.nome} é de R${self.preco_kg} o kg e tem {self.estoque_kg} kg em estoque")


fruta1 = Fruta("Kiwi", 5, 20)

fruta1.exibir() # O preço da fruta Kiwi é de R$5 o kg e tem 20 kg em estoque

fruta2 = Fruta("Pêssego", 3, 43)

Fruta.exibir(fruta2) # O preço da fruta Pêssego é de R$3 o kg e tem 43 kg em estoque
