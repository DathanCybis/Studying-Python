class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    




def main():
    estudantes = []

    while True:
        print("\n --- Menu --- ")
        print("1. Adicionar um novo estudante")
        print("2. Atualizar a nota de um estudante existente")
        print("3. Visualizar informações de um estudante")
        print("4. Listar todos os estudantes")
        print("5. Sair\n")

        opc = input("Digite a opção desejada: ")

        if opc == "1":
            pass
        elif opc == "2":
            pass
        elif opc == "3":
            pass
        elif opc == "4":
            pass
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, opção inválida!")
