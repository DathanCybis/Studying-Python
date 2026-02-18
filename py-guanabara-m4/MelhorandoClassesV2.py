class ContaBancaria:
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo

    
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")


    def sacar(self, valor):
        if self.saldo - valor < 0:
            print(f"Saque de R${valor:,.2f} não autorizado!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")


c1 = ContaBancaria(112, "Gustavo", 3000)
c1.depositar(500)
c1.sacar(1500)
print(c1)
c1.sacar(2001)
print(c1)
