#1.
animal = {
    "tipo": "gato",
    "cor": "preto",
    "idade": 3
}
print(animal) # Saída: {'tipo': 'gato', 'cor': 'preto', 'idade': 3}

print()

#2.
estudante = {}

estudante["nome"] = "Carlos"
estudante["curso"] = "Matemática"
estudante["semestre"] = 2
print(estudante) # Saída: {'nome': 'Carlos', 'curso': 'Matemática', 'semestre': 2}

print()

#3.
universidade = {

    "nome": "Universidade Paulista",
    "localidade": {
        "cidade": "Araraquara",
        "bairro": "Parque das Laranjeiras"
    }
}
print(universidade) # Saída: {'nome': 'Universidade Paulista', 'localidade': {'cidade': 'Araraquara', 'bairro': 'Parque das Laranjeiras'}}
print(universidade["nome"]) # Saída: Universidade Paulista
print(universidade["localidade"]["cidade"]) # Saída: Araraquara
