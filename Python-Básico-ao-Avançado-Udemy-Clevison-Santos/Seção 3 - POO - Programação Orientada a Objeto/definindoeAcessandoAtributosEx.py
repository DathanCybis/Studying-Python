class Fruta:
    def __init__(self, nome, preco_kg, estoque_kg):
        self.nome = nome
        self.preco_kg = preco_kg
        self.estoque_kg = estoque_kg


fruta1 = Fruta("Kiwi", 5, 20)

print(f"O preço da fruta {fruta1.nome} é de R${fruta1.preco_kg} o kg e tem {fruta1.estoque_kg} kg em estoque") # O preço da fruta Kiwi é de R$5 o kg e tem 20 kg em estoque

fruta2 = Fruta("Pêssego", 3, 43)

print(f"O preço da fruta {fruta2.nome} é de R${fruta2.preco_kg} o kg e tem {fruta2.estoque_kg} kg em estoque") # O preço da fruta Pêssego é de R$3 o kg e tem 43 kg em estoque
