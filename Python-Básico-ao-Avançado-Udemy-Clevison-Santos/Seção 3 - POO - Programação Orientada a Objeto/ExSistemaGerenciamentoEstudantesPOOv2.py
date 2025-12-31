alunos = []
class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota


    def get_nome(self):
        return self.nome

    
    def get_idade(self):
        return self.idade
    

    def get_nota(self):
        return self.nota
    

    def set_nome(self, nome):
        self.nome = nome

    
    def set_idade(self, idade):
        self.idade = idade
    

    def set_nota(self, nota):
        self.nota = nota
    

def menu():
    estudantes = []

    while True:
        print("\n --- Menu --- ")
        print("1. Adicionar um novo estudante")
        print("2. Atualizar a nota de um estudante existente")
        print("3. Visualizar informações de um estudante")
        print("4. Listar todos os estudantes")
        print("5. Sair")

        opc = input("\nDigite a opção desejada: ")

        if opc == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            nota = float(input("Nota: "))

            novo_estudante = Estudante(nome, idade, nota)

            estudantes.append(novo_estudante)

            print(f"Estudante {nome} adicionado com sucesso!")


        elif opc == "2":
            pass

    
        elif opc == "3":
            estudante.visualizar_estudante()
        elif opc == "4":
            estudante.listar_estudantes()
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, opção inválida!")


menu()
