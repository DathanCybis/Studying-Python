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
            remover_contato()
        elif opc == 4:
            listar_contato()
        elif opc == 5:
            print("\nSaindo...\n")
            break
        else:
            print("Digite uma opção válida.")


def adicionar_contato():
    nome = str(input("Digite o nome: "))
    numero = int(input("Digite o número: "))

    if nome in agenda:
        print("\nErro ao adicionar! Contato já existente!")
        return

    agenda[nome] = numero

    print("\nContato adicionado com sucesso!")


def editar_contato():
    listar_contato()
    nome = input("Digite o nome a ser mudado: ")
    if nome in agenda:
        nome_novo = input("Digite o novo nome (Deixa em branco para manter): ")
        numero = input("Digite o número (Deixe em branco para manter): ")

        if nome_novo:
            if nome_novo in agenda:
                print("\nErro ao editar! O nome digitado já está em uso!")
                return
            
            agenda[nome_novo] = agenda.pop(nome)
        else:
            nome_novo = nome

        if numero:
            agenda[nome_novo] = numero

        print("\nContato atualizado com sucesso!")
    else:
        print("\nContato não existente!")


def remover_contato():
    listar_contato()
    nome = str(input("Digite o nome do contato a ser excluído: "))

    if nome in agenda:
        agenda.pop(nome) #or del agenda[nome]
        print("\nContato removido com sucesso!")
    else:
        print("\nContato não existente!")

def listar_contato():
    print("\n")

    if not agenda:
        print("Nenhum contato registrado!")

    for chave, valor in agenda.items():
        print(f"Nome: {chave}")
        print(f"Telefone: {valor}\n")


def main():
    global agenda
    agenda = {}
    selecionar_menu()


main()
