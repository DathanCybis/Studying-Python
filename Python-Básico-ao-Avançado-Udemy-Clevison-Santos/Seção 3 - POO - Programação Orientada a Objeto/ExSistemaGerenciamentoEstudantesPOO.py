alunos = []
class Estudante:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.nota = 0.0

    
    def adicionar_estudante(self):
        nome = input("Digite o nome do estudante: ")
        try:
            idade = int(input("Digite a idade do estudante: "))
            if idade > 0:
                pass
            else:
                print("Digite um número inteiro válido.")
                idade = 0
        except:
            print("Digite um número inteiro válido.")

        try:
            nota = float(input("Digite a nota do estudante: "))
            if nota > 0 and nota <= 10:
                pass
            else:
                print("Digite uma nota válida.")
                nota = 0.0
        except:
            print("Digite um número flutuante válido.")

        alunos.append([nome, idade, nota])
        print("Estudante adicionado com sucesso!")


    def atualizar_nota(self):
        nome = input("Digite o nome do estudante que deseja atualizar a nota: ")

        try:
            nota = float(input("Digite a nota do estudante: "))
            if nota > 0 and nota <= 10:
                for i, v in enumerate(alunos):
                    if alunos[i][0] == nome:
                        alunos[i][2] = nota
                print("Nota atualizada com sucesso!")
        except:
            print("Digite um número flutuante válido.")


    def visualizar_estudante(self):
        nome = input("Digite o nome do estudante que deseja atualizar a nota: ")
        for i, v in enumerate(alunos):
            if alunos[i][0] == nome:
                print(f"Nome: {v[0]}, Idade: {v[1]}, Nota: {v[2]}")
            else:
                print("Aluno não encontrado.")
        

    def listar_estudantes(self):
        if alunos:
            for n in alunos:
                print(f"Nome: {n[0]}, Idade: {n[1]}, Nota: {n[2]}")
        else:
            print("Nenhum aluno foi cadastrado!")


def main():

    while True:
        estudante = Estudante()
        print("\n --- Menu --- ")
        print("1. Adicionar um novo estudante")
        print("2. Atualizar a nota de um estudante existente")
        print("3. Visualizar informações de um estudante")
        print("4. Listar todos os estudantes")
        print("5. Sair\n")

        opc = input("Digite a opção desejada: ")

        if opc == "1":
            estudante.adicionar_estudante()
        elif opc == "2":
            estudante.atualizar_nota()
        elif opc == "3":
            estudante.visualizar_estudante()
        elif opc == "4":
            estudante.listar_estudantes()
        elif opc == "5":
            print("Saindo...")
            break
        else:
            print("Tente novamente, opção inválida!")


main()
