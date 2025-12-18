class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
        self.__saldo = 0


    def mostrar_nome(self):
        return self.nome


    def mostrar_idade(self):
        return self._idade
    

    def _aumentar_idade(self):
        self._idade += 1


    def __aumentar_saldo(self, quant):
        self.__saldo += quant


    def depositar(self, quant):
        self.__aumentar_saldo(quant)

        return self.__saldo
    

p = Pessoa("Alice", 30)

print(p.nome) # Alice

print(p._idade) # 30 #Não recomendado

print(p._Pessoa__saldo) # 0 #Não recomendado


# --- Métodos Públicos --- 
print("\nMétodos Públicos:")
print(p.mostrar_nome()) # Alice
print(p.mostrar_idade()) # 30
print(p.depositar(1500)) # 1500
print(p.depositar(1000)) # 2500
print(p.depositar(3500)) # 6000

# --- Métodos Privados --- 
print("\nMétodos Privados:")
