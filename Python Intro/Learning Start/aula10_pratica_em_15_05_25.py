# pedir uma string (palavra) ao usuario
# compare o 2º caractere ([1]) com o penultimo ([-2])
# informe se são iguais ou diferentes

entrada = input("Digite uma palavra ou frase: ")

penultimo = len(entrada) - 2

# verifica se tem pelo menos 2 caracteres
if entrada[penultimo] == entrada[1]:
    print(f"São iguais letra 1: {entrada[penultimo]} e a letra 2: {entrada[1]} ")
else:
    print(f"Não são iguais letra 1: {entrada[penultimo]} e a letra 2: {entrada[1]} ")
    