class Animal():
    def __init__(self, animal, som):
        self.animal = animal
        self.som = som


    def fazer_som(self):
        print(f"O {self.animal} faz {self.som}")


class Cachorro(Animal):
    def __init__(self):
        self.animal = "Cachorro"
        self.som = "Au Au"

    
    def latir(self):
        print("Woof-Woof")


    def fazer_som(self):
        print(f"O {self.animal} faz {self.som}")


class Gato(Animal):
    def __init__(self):
        self.animal = "Gato"
        self.som = "Miau"


    def miar(self):
        print("Miauuuu")


    def fazer_som(self):
        print(f"O {self.animal} faz {self.som}")


animal = Animal("Porco", "Oinc-Oinc")
animal.fazer_som() # O Porco faz Oinc-Oinc

print()

cachorro = Cachorro()
cachorro.fazer_som() # O Cachorro faz Au Au
cachorro.latir() # Woof-Woof

print()

gato = Gato()
gato.fazer_som() # O Gato faz Miau
gato.miar() # Miauuuu
