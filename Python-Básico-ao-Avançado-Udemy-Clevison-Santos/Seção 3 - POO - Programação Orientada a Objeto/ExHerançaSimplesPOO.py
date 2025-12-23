class Animal():
    def fazer_som(self):
        print(f"O animal faz um som")


class Cachorro(Animal):
    def latir(self):
        print("Woof-Woof")


    def fazer_som(self):
        print("O cachorro faz Au-Au")


class Gato(Animal):
    def miar(self):
        print("Miauuuu")


    def fazer_som(self):
        print(f"O gato faz miau")


animal = Animal()
animal.fazer_som() # O animal faz um som

print()

cachorro = Cachorro()
cachorro.fazer_som() # O Cachorro faz Au Au
cachorro.latir() # Woof-Woof

print()

gato = Gato()
gato.fazer_som() # O Gato faz miau
gato.miar() # Miauuuu
