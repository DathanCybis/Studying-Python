def funcao_externa():

    variavel_externa = "Eu sou externa"

    print(variavel_externa) # <<<<<

    def funcao_interna():
        
        nonlocal variavel_externa

        variavel_externa = "Eu fui modificado pela funcao_interna"

        print(variavel_externa) # <<<<<
    
    funcao_interna()

    print(variavel_externa) # <<<<<

funcao_externa()
