class Impressora:
    def imprimir(self, arg):
        if isinstance(arg, str):
            print(f"Imprimindo texto: {arg}")
        elif isinstance(arg, list):
            print("Imprimindo lista de textos:")

            for item in arg:
                print(f" - {item}")

        elif isinstance(arg, dict):
            print("Imprimindo dicionários de textos:")

            for i, j in arg.items():
                print(f" - {i}: {j}")
        else:
            print("Tipo de dado não suportado para impressão")


imp = Impressora()

imp.imprimir("teste") # Imprimindo texto: teste

imp.imprimir(["testando", "12"]) # Imprimindo lista de textos: \n  - testando \n  - 12

imp.imprimir({"testes": "23"}) # Imprimindo dicionários de textos: \n  - testes: 23
