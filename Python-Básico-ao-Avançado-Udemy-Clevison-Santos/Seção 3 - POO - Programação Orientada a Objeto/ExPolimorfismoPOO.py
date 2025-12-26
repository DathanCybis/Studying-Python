class Impressora:
    def imprimir(self, arg):
        if isinstance(arg, str):
            print("É uma string")
        elif isinstance(arg, list):
            print("É uma lista")
        elif isinstance(arg, dict):
            print("É um dicionário")
        else:
            print("Nenhuma opção encontrada!")


imp = Impressora()

imp.imprimir("teste") # É uma string

imp.imprimir(["testando", "12"]) # É uma lista

imp.imprimir({"teste": 12}) # É um dicionário
