class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda():
    def __init__(self):
        self.contatos = []


    def adicionar_contatos(self, contato):
        self.contatos.append(contato)


    def remover_contatos(self, nome):
        for contato in self.contatos:

            if contato.nome == nome:
                self.contatos.remove(contato)
                return True

        return False


    def listar_contatos(self):
        return self.contatos
        

    def buscar_contatos(self, nome):
        for contato in self.contatos:

            if contato.nome == nome:
                return contato
            
        return None


def menu():
    agenda = Agenda()
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

            novo_contato = Contato(nome, telefone, email)
            agenda.adicionar_contatos(novo_contato)

            print("Contato adicionado com sucesso!")


        elif opc == "2":
            nome = input("Nome do contato que deseja excluir: ")

            if agenda.remover_contatos(nome):
                print("Contato removido com sucesso.")
            else:
                print("Contato não encontrado.")


        elif opc == "3":
            print("Listando todos os contatos...")

            for contato in agenda.listar_contatos():
                    print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")


        elif opc == "4":
            nome = input("Nome do contato que deseja encontrar: ")

            contato = agenda.buscar_contatos(nome)

            if contato:
                print(f"Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}")
            else:
                print("Contato não encontrado.")


        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, por favor digite uma opção válida!")


if __name__ == "__main__":
    menu()
