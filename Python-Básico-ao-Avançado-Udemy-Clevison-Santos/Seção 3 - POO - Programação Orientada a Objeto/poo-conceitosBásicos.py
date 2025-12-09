#1. Classes e Objetos
class Livro:
    
    def __init__(self, titulo, autor, ano):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

meu_livro = Livro("1984", "George Orwell", 1949)

#2. Atributos
print(meu_livro.titulo) # 1984
print(meu_livro.autor) # George Orwell
print(meu_livro.ano) # 1949

#3. Métodos
class Livro:
    
    def __init__(self, titulo, autor, ano):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    
    def descricao(self):
        return f"'{self.titulo}', por '{self.autor}', publicado em '{self.ano}'"


meu_livro = Livro("1984", "George Orwell", 1949)

print(meu_livro.descricao()) # '1984', por 'George Orwell', publicado em '1949'
