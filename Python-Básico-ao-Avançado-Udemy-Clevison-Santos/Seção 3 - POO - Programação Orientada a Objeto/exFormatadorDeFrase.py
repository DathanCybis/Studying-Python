class FormatadorDeFrase:
    def __init__(self, frase):
        self.frase = frase

    
    def maiusculas(self):
        print(f"Frase atual: {self.frase}".upper())


    def minusculas(self):
        print(f"Frase atual: {self.frase}".lower())


    def capitalizadas(self):
        print(f"Frase atual: {self.frase}".capitalize())


    def titulo(self):
        print(f"Frase atual: {self.frase}".title())


    def contar_vogais(self):
        count = 0
        for i in self.frase.lower():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count += 1
            elif i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú":
                count += 1
        print(f"A frase contém {count} vogais!")
        print(f"Frase atual: {self.frase}")


    def contar_consoantes(self):
        count = len(self.frase)
        for i in self.frase.lower():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count -= 1
            elif i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú":
                count -= 1
        print(f"A frase contém {count} consoantes!")
        print(f"Frase atual: {self.frase}")


    def contar_a(self):
        print(f"A frase contém {self.frase.lower().count("a")} letra(s) 'A'")
        print(f"Frase atual: {self.frase}")


    def procurar_frase(self):
        procurar = input("Qual frase deseja procurar: ")

        print(f"A palavra '{procurar}' aparece {self.frase.count(procurar)} vez(es) na frase.")
        print(f"Frase atual: {self.frase}")


    def mostrar_frase(self):
        print(f"Frase atual: {self.frase}")


frases = FormatadorDeFrase("Python é muito legal!")

frases.maiusculas()

frases.minusculas()

frases.capitalizadas()

frases.titulo()

frases.contar_vogais()

frases.contar_consoantes()

frases.contar_a()

frases.mostrar_frase()

frases.procurar_frase()
