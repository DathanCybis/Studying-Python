class Termostato:
    def __init__(self, temperatura_atual=20):
        self.temperatura_atual = temperatura_atual


    def aumentar_temperatura(self, valor):
        self.temperatura_atual += valor
        print(f"Temperatura aumentada em: {valor}°, Nova temperatura: {self.temperatura_atual}°")


    def diminuir_temperatura(self, valor):
        self.temperatura_atual -= valor
        print(f"Temperatura diminuída em: {valor}°, Nova temperatura: {self.temperatura_atual}°")


meu_termostato = Termostato()

meu_termostato.aumentar_temperatura(5) # Temperatura aumentada em: 5°, Nova temperatura: 25°

meu_termostato.diminuir_temperatura(5) # Temperatura diminuída em: 5°, Nova temperatura: 20°
