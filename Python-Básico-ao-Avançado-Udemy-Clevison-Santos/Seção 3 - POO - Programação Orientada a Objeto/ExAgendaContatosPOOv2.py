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


