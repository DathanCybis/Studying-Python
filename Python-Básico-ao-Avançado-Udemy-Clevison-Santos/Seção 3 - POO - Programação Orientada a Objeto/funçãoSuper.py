class Animal:
    def falar(self):
        print("O animal está falando")


class Cachorro(Animal):
    def falar(self):
        super().falar()
        print("O cachorro diz 'Au Au'")


animal = Animal()

animal.falar() # O animal está falando

print()

cachorro = Cachorro()

cachorro.falar() # O animal está falando \n # O cachorro diz 'Au Au'
