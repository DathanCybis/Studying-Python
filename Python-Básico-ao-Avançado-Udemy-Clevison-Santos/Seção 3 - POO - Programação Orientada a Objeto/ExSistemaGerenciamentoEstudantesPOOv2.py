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
            nome = input("Digite o nome do estudante que deseja atualizar a nota: ")

            for estudante in estudantes:
                if estudante.get_nome() == nome:
                    nova_nota = float(input("Digite a nova nota: "))

                    estudante.set_nota(nova_nota)

                    print(f"Nota atualizada com sucesso!")
                break
            else:
                print("Estudante não encontrado!")        
    
        elif opc == "3":
            nome = input("Digite o nome do estudante para visualizar as informações: ")

            for estudante in estudantes:
                if estudante.get_nome() == nome:
                    print(f"Nome: {estudante.get_nome()}, Idade: {estudante.get_idade()}, Nota: {estudante.get_nota()}")
                break
            else:
                print("Estudante não encontrado!")


        elif opc == "4":
            print("Listando todos os estudantes: ")

            if estudantes:
                for n in estudantes:
                    print(f"Nome: {n[0]}, Idade: {n[1]}, Nota: {n[2]}")
            else:
                print("Nenhum aluno foi cadastrado!")



        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, opção inválida!")


menu()
