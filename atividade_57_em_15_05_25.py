# peça uma string ao usuário
# se ela tiver menos que 20 caracteres, complete o início da linha com * até dar 20
# se ela tiver mais que 20 caracteres, mostre apenas os ultimos 20 caracteres da SyntaxWarning

texto = input("Digite uma string: ")

if len(texto) < 20:
    asteriscos = "*" * (20 - len(texto))
    resultado = asteriscos + texto
else:
    resultado = texto[-20:]

print("Resultado formatado: ", resultado)
