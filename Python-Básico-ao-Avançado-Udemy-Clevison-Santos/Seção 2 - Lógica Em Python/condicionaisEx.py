convite_vip = str(input("Você tem um convite VIP?: ")).strip().lower()
lista_convidados = str(input("Você está na lista de convidados?: ")).strip().lower()
membro_clube = str(input("Você é um membro do clube?: ")).strip().lower()

if "sim" in convite_vip or "sim" in lista_convidados or "sim" in membro_clube:
    print("Bem vindo(a) ao evento!")
else:
    print("Desculpe, você não pode entrar no evento.")
