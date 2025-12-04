def mostrar_menu():
    print("\nMENU: ")
    print("1. Adicionar contato")
    print("2. Editar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair\n")


def selecionar_menu():
    while True:
        mostrar_menu()
        opc = int(input("Selecione a opção desejada: "))

        if opc == 1:
            adicionar_contato()
        elif opc == 2:
            editar_contato()
        elif opc == 3:
            pass
        elif opc == 4:
            listar_contato()
        elif opc == 5:
            break
        else:
            print("Digite uma opção válida.")


def adicionar_contato():
    nome = str(input("Digite o nome: "))
    numero = int(input("Digite o número: "))

    agenda[nome] = numero


def editar_contato():
    listar_contato()
    nome = str(input("Digite o nome a ser mudado: "))
    nome_novo = str(input("Digite o novo nome: "))
    numero = int(input("Digite o número: "))

    agenda[nome_novo] = agenda.pop(nome)
    agenda[nome_novo] = numero

def listar_contato():
    print(agenda)


agenda = {}


selecionar_menu()
