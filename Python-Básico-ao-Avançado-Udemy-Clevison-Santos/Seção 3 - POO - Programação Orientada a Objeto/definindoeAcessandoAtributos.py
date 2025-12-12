class Jogador:
    def __init__(self, nome, posicao, numero_camisa, gols=0):
        self.nome = nome
        self.posicao = posicao
        self.numero_camisa = numero_camisa
        self.gols = gols

jogador1 = Jogador("Roberto", "Atacante", 9)

jogador2 = Jogador("Carlos", "Goleiro", 1)

print(f"{jogador1.nome} é um {jogador1.posicao} com a camisa de número {jogador1.numero_camisa}") # Roberto é um Atacante com a camisa de número 9

print(f"{jogador2.nome} é um {jogador2.posicao} com a camisa de número {jogador2.numero_camisa}") # Carlos é um Goleiro com a camisa de número 1

jogador1.gols += 1
jogador1.gols += 1
jogador1.gols += 1

print(f"{jogador1.nome} marcou {jogador1.gols} gol(s)") # Roberto marcou 3 gol(s)

jogador2.gols += 2

print(f"{jogador2.nome} marcou {jogador2.gols} gol(s)") # Carlos marcou 2 gol(s)
