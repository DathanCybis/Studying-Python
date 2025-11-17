#Split e Join

palavras = ['Olá,', 'como', 'vai', 'você?']
frase = ' '.join(palavras)

print(frase)


texto = '*****Olá*****'
texto_strip = texto.strip('*')

print(texto_strip)

print()

frase2 = 'Olá, Mundo!'

parte = frase2[4:8]
print(parte)

primeiros = frase2[:5]
print(primeiros)

ultimos = frase2[-6:]
print(ultimos)
