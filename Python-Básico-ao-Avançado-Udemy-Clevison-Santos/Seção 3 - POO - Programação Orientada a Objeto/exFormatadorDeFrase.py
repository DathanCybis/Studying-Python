class FormatadorDeFrase:
    def __init__(self, frase):
        self.frase = frase

    
    def maiusculas(self):
        print(f"{self.frase}".upper())


    def minusculas(self):
        print(f"{self.frase}".lower())


    def capitalizadas(self):
        print(f"{self.frase}".capitalize())


    def titulo(self):
        print(f"{self.frase}".title())


    def contar_vogais(self):
        count = 0
        for i in self.frase.lower():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count += 1
            elif i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú":
                count += 1
        print(f"A frase contém {count} vogais!")


    def contar_consoantes(self):
        count = len(self.frase)
        for i in self.frase.lower():
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                count -= 1
        print(f"A frase contém {count} consoantes!")





frases = FormatadorDeFrase("Python é muito legal!")

frases.maiusculas()

frases.contar_vogais()

frases.contar_consoantes()
