livros = {
    "título": "livro",
    "autor": "alguém",
    "lancamento": "algum dia"
}

print(livros) # {'título': 'livro', 'autor': 'alguém', 'lancamento': 'algum dia'}

participantes = {
    "fulano": "sem nome",
    "beltrano": "nome algum"
}

livros.update(participantes)

print(livros) # {'título': 'livro', 'autor': 'alguém', 'lancamento': 'algum dia', 'fulano': 'sem nome', 'beltrano': 'nome algum'}
