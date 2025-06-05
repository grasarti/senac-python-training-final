# escrever uma função chamada conta_elementos_match(minha_matriz: list, elemento: int) 
# que recebe um array bidimensional de inteiros e um unico valor inteiro como seus argumentos
# a função então conta quantos elementos dentro da matriz correspondem ao valor do argumento


def conta_elementos_match(minha_matriz: list, elemento: int) -> int:
    contador = 0        # começa com zero ocorrência
    
    for linha in minha_matriz:
        for item in linha:
            if item == elemento:        # verifica se o item é igual ao valor procurado
                contador += 1
                
        return contador         # retorna a contagem total

# exemplo
matriz = [
    [1, 2, 3],
    [4, 1, 6],
    [7, 8, 1]
]

print(conta_elementos_match(matriz, 1))     # saída: 3      o número 1 aparece 3 vezes na matriz
    