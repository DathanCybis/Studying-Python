def classificarNum(n):

    if n < 0:
        return "Negativo"
    elif n == 0:
        return "Zero"
    else:
        return "Positivo"
    
print("Função Regular:", classificarNum(-2)) # Saída: Negativo

# Função Lambda:

classificarNum_lambda = lambda n: "Negativo" if n < 0 else ("Zero" if n == 0 else "Positivo")

print("Função Lambda: ", classificarNum_lambda(2)) # Saída: Positivo
