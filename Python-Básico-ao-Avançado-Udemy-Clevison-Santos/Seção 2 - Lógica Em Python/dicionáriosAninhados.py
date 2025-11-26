familia = {

    "pai": {
        "nome": "Roberto",
        "idade": 50
    },
    
    "mae": {
        "nome": "Patrícia",
        "idade": 52
    },

    "filho": {
        "nome": "Nicolas",
        "idade": 27
    }
}
print(familia) # Saída: {'pai': {'nome': 'Roberto', 'idade': 50}, 'mae': {'nome': 'Patrícia', 'idade': 52}, 'filho': {'nome': 'Nicolas', 'idade': 27}}
print(familia["pai"]) # Saída: {'nome': 'Roberto', 'idade': 50}
print(familia["pai"]["nome"]) # Saída: Roberto
