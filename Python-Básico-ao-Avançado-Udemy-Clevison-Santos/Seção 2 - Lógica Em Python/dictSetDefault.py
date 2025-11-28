livros = {
    "título": "livro",
    "autor": "alguém",
    "lancamento": "algum dia"
}

print(livros) # {'título': 'livro', 'autor': 'alguém', 'lancamento': 'algum dia'}

pessoa = livros.setdefault("sucesso", "talvez")

print(pessoa) # talvez

print(livros) # {'título': 'livro', 'autor': 'alguém', 'lancamento': 'algum dia', 'sucesso': 'talvez'}
