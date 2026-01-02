class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


    def get_nome(self):
        return self.nome


    def get_telefone(self):
        return self.telefone
    

    def get_email(self):
        return self.email
    

    def set_nome(self, nome):
        self.nome = nome


    def set_telefone(self, telefone):
        self.telefone = telefone


    def set_email(self, email):
        self.email = email


class Agenda(Contato):
    def adicionar_contatos(self, nome, telefone, email):
        super().set_nome(nome)
        super().set_telefone(telefone)
        super().set_email(email)


    def remover_contatos(self):
        pass

    def listar_contatos(self):
        super().get_nome()

    def buscar_contatos(self):
        pass


def menu():
    contatos = []
    while True:
        print("\n1. Adicionar contatos")
        print("2. Remover contatos")
        print("3. Listar contatos")
        print("4. Buscar contato")
        print("5. Sair\n")

        opc = input("Digite a opção desejada: ")

        print()

        if opc == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")

            novo_contato = Agenda(nome, telefone, email)
            contatos.append(novo_contato)

            print("Contato adicionado com sucesso!")


        elif opc == "2":
            pass


        elif opc == "3":
            print("Listando todos os contatos...")

            if contatos:
                for contato in contatos:
                    print(f"Nome: {contato.get_nome()}, Telefone: {contato.get_telefone()}, Email: {contato.get_email()}")
            else:
                print("Nenhum contato foi cadastrado.")


        elif opc == "4":
            pass


        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, por favor digite uma opção válida!")


menu()
