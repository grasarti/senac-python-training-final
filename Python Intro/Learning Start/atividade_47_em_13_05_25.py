# entrada de dados
limite = int(input("Digite o limite: "))

# comeca em 1
numero = 1

# enquanto o numero for menor ou igual ao limite
while numero <= limite:
    print(numero)
    numero *= 2 #dobra o valor de cada passo
print(f" O limite era: {limite}")