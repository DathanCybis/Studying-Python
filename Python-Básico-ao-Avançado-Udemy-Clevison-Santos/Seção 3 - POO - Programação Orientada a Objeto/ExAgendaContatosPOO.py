class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda:
    def adicionar_contatos(self):
        pass

    def remover_contatos(self):
        pass

    def listar_contatos(self):
        pass

    def buscar_contatos(self):
        pass


def menu():
    agenda = Agenda()
    while True:
        print("1. Adicionar contatos")
        print("2. Remover contatos")
        print("3. Listar contatos")
        print("4. Buscar contato")
        print("5. Sair")

        opc = input("Digite a opção desejada: ")

        if opc == "1":
            agenda.adicionar_contatos()
        elif opc == "2":
            agenda.remover_contatos()
        elif opc == "3":
            agenda.listar_contatos()
        elif opc == "4":
            agenda.buscar_contatos()
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, por favor digite uma opção válida!")


menu()
