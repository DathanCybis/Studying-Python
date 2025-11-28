def criar_perfil(nome, idade, email):

    return {
        "nome": nome,
        "idade": idade,
        "email": email
    }

novo_usuario = criar_perfil("Paulo", 32, "paulo@email.com")

print(novo_usuario) # {'nome': 'Paulo', 'idade': 32, 'email': 'paulo@email.com'}
