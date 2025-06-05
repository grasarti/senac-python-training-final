# Crie uma função chamada linha que:
# Receba 2 parâmetros:
#     - Um número inteiro (tamanho da linha)
#     - Uma string (que será o caractere a ser usado)

# Imprima um linha com o caractere reptido n vezes;
# Se a string for fazia, use *


def linha(n, caractere):
    if caractere == "":
        caractere = "*"
    else:
        caractere = caractere[0]
    print(caractere * n)
    
linha(6, "x")
linha(5, "%")
linha(9, "L")