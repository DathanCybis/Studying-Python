class Musico:
    def tocar_instrumento(self):
        print("Tocando instrumento musical")


class Atleta:
    def correr(self):
        print("Correndo na pista")



class MusicoAtleta(Musico, Atleta):
    def exibir_habilidades(self):
        print("Tocando instrumento e correndo")


musicoAtleta = MusicoAtleta()

musicoAtleta.tocar_instrumento() # Tocando instrumento musical

musicoAtleta.correr() # Correndo na pista

musicoAtleta.exibir_habilidades() # Tocando instrumento e correndo

