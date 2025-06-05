# pedir ao usuário para digitar números até que a lista esteja em ordem decrescente
# ou seja, o último número digitado for menor que o anterior
# ao final, imprimir todos os número em ordem crescente

def lista_crescente():
    numeros = []

    while True:
        numero = int(input("Digite um número: "))
        numeros.append(numero)
    
        if len(numeros) > 1 and numeros[-1] < numeros[-2]:
            break
    
    numeros_ordenados = sorted(numeros)
    print("Números digitados (ordem crescente):", numeros_ordenados)

lista_crescente()