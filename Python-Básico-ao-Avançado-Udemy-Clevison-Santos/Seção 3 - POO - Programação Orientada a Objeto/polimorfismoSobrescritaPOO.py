class Animal():
    def som(self):
        print("O animal faz um som")

        
class Cachorro(Animal):
    def som(self):
        print("O cachorro late")

        
class Gato(Animal):
    def som(self):
        print("O gato mia")


animal = Animal()

animal.som() # O animal faz um som

cachorro = Cachorro()

cachorro.som() # O cachorro late

gato = Gato()

gato.som() # O gato mia
