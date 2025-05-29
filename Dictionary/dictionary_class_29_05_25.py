# dicionário

# usado para armazenar dados no formato: Chave:valor 
# são ordenados
# mutáveis
# não permite elementos duplicados

meu_dicionario = {}
meu_dicionario["apina"] = "macaco"
meu_dicionario["nome"] = "Graci"

# print(meu_dicionario)
# print(meu_dicionario["nome"])

palavra = input("Digite uma palavra: ")

if palavra in meu_dicionario:
    
    print("Tradução:", meu_dicionario[palavra])

else:
    print("Palavra não encontrada")
    
resultado = {}
resultado["maria"] = 5
resultado["julia"] = 10

soma = resultado["maria"] + resultado["Julia"]

# imprimir chave valor

dicionario = {}

dicionario["apina"] = "Macaco"
dicionario["banana"] = "Amarela"
dicionario["cembalo"] = "Cravo"

for chave in dicionario:
    print("Chave:",chave)
    print("Valor", dicionario[chave])
    