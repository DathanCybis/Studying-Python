class Termostato:
    def __init__(self, temperatura_atual=20):
        self.temperatura_atual = temperatura_atual


    def aumentar_temperatura(self, valor):
        self.temperatura_atual += valor
        print(f"Temperatura aumentada em: {valor}°, Nova temperatura: {self.temperatura_atual}°")


    def diminuir_temperatura(self, valor):
        self.temperatura_atual -= valor
        print(f"Temperatura diminuída em: {valor}°, Nova temperatura: {self.temperatura_atual}°")


    def configurar_temperatura(self, nova_temperatura):
        self.temperatura_atual = nova_temperatura
        print(f"Temperatura configurada para {nova_temperatura}°")


meu_termostato = Termostato()

meu_termostato.aumentar_temperatura(5) # Temperatura aumentada em: 5°, Nova temperatura: 25°

meu_termostato.diminuir_temperatura(5) # Temperatura diminuída em: 5°, Nova temperatura: 20°

meu_termostato.configurar_temperatura(19) # Temperatura configurada para 19°
