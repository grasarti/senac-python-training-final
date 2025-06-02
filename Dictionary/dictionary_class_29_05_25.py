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
    

# Dicionários arquivados dentro de listas

# pessoa1 = {"nome": "Pippa Python", "altura": 154, "peso": 61, "idade": 44}
# pessoa2 = {"nome": "Peter Pythons", "altura": 174, "peso": 103, "idade": 31}
# pessoa3 = {"nome": "Pedro Python", "altura": 191, "peso": 71, "idade": 14}
# pessoas = [pessoa1, pessoa2, pessoa3]
 
# for pessoa in pessoas:
#     print(pessoa["nome"])
 
# altura_combinada = 0
# for pessoa in pessoas:
#     altura_combinada += pessoa["altura"]
# print("A altura média é", altura_combinada / len(pessoas))
 