# escrever um programa que peça ao usuário um número inteiro positivo N
# o programa deve imprimir todos os números entre -N e N, exceto o número 0
# cada número deve aparecer numa linha separada

n = int(input("Digite um número inteiro positivo: "))
for i in range(-n, n + 1):
    if i != 0:
        print(i)

# o número 0 é ignorado, como o enunciado pede

n = int(input("Digite um número inteiro positivo: "))
for i in range(-n, n + 1):
    if i != 0:
        print(i,end=" ")