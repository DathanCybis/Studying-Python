precos = {
    "teclado": 50.0,
    "mouse": 25.0,
    "placa de video": 1250.0,
    "memoria ram": 675.0
}

print(precos) # {'teclado': 50.0, 'mouse': 25.0, 'placa de video': 1250.0, 'memoria ram': 675.0}

caros = {item: preco for item, preco in precos.items() if preco > 50}

print(caros) # {'placa de video': 1250.0, 'memoria ram': 675.0}
