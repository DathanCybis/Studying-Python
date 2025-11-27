livros = {
    "titílo": "livro",
    "autor": "alguém",
    "lancamento": "algum dia"
}

print(livros) # {'titílo': 'livro', 'autor': 'alguém', 'lancamento': 'algum dia'}

pessoa = livros.setdefault("sucesso", "talvez")

print(pessoa) # talvez

print(livros) # {'titílo': 'livro', 'autor': 'alguém', 'lancamento': 'algum dia', 'sucesso': 'talvez'}
