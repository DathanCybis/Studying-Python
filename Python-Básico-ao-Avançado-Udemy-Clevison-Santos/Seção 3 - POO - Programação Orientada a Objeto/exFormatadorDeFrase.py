class FormatadorDeFrase:
    def __init__(self, frase):
        self.frase = frase

    
    def maiusculas(self):
        self.frase = self.frase.upper()


    def minusculas(self):
        self.frase = self.frase.lower()


    def capitalizadas(self):
        self.frase = self.frase.capitalize()


    def titulo(self):
        self.frase = self.frase.title()


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
            elif i == "á" or i == "é" or i == "í" or i == "ó" or i == "ú":
                count -= 1
        print(f"A frase contém {count} consoantes!")


    def contar_a(self):
        print(f"A frase contém {self.frase.lower().count("a")} letra(s) 'A'")


    def procurar_frase(self):
        procurar = input("Qual frase deseja procurar: ")

        print(f"A palavra '{procurar}' aparece {self.frase.count(procurar)} vez(es) na frase.")


    def mostrar_frase(self):
        return self.frase


def main():
    frase = input("Digite uma frase: ")
    
    frases = FormatadorDeFrase(frase)

    while True:
        print("\nEscolha uma opção para formatar sua frase:")
        print("1. Converter para maiúsculas")
        print("2. Converter para minúsculas")
        print("3. Capitalizar a primeira letra")
        print("4. Converter para formato de título")
        print("5. Contar vogais")
        print("6. Contar consoantes")
        print("7. Contar letra 'a'")
        print("8. Pesquisar palavra")
        print("9. Mostrar frase atual")
        print("10. Sair")

        opc = input("\nDigite qual opção quer escolher: ")

        if opc == "1":
            frases.maiusculas()
        elif opc == "2":
            frases.minusculas()
        elif opc == "3":
            frases.capitalizadas()
        elif opc == "4":
            frases.titulo()
        elif opc == "5":
            frases.contar_vogais()
        elif opc == "6":
            frases.contar_consoantes()
        elif opc == "7":
            frases.contar_a()
        elif opc == "8":
            frases.procurar_frase()
        elif opc == "9":
            frases.mostrar_frase()
        elif opc == "10":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

        print("Frase atual:", frases.mostrar_frase())


if __name__ == "__main__":    
    main()
