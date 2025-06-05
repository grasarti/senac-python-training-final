# entrada de dados
limite = int(input("Digite o limite: "))
base = int(input("Digite a base de multiplicação: "))

# comeca em 1
numero = 1

# enquanto o numero for menor ou igual ao limite
while numero <= limite:
    print(numero)
    numero *= base # multiplica pela base informada
print(f"O limite era: {limite}")