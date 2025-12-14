class Termostato:
    def __init__(self, temperatura_atual=20):
        self.temperatura_atual = temperatura_atual

    def aumentar_temperatura(self, valor):
        self.temperatura_atual += valor
        print(f"Temperatura aumentada em: {valor}, Nova temperatura: {self.temperatura_atual}")

    