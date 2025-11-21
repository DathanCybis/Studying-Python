# Retornando funções de outras funções

def nivel_saudacao(nivel):

    def saudacao_basica():
        return "Oi!"
    
    def saudacao_avancada():
        return "Olá, como você está?"
    
    
    if str(nivel).lower() == "basica":

        return saudacao_basica

    else:

        return saudacao_avancada


cumprimento = nivel_saudacao("basica")
print(cumprimento())

cumprimento = nivel_saudacao("avancada")
print(cumprimento())
