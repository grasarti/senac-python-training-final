# Peça ao usuário digitar város números
# Continue somando esses números
# Pare quando a soma for maior que 100
# Mostre a soma total ao final

# Inicializa a variável da soma
soma = 0

# Enquanto a soma for menor ou igual a 100
while soma <= 100:
    numero = int(input("Digite um número: "))
    soma += numero # adiciona o numero a soma
    
# Exibe o resultado final
print(f"A soma total é: {soma}")

