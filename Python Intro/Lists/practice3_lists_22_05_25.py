# Lista para armazenar os valores digitados
valores = []

while True:
    # Solicita o valor ao usuário
    numero = int(input("Digite um número (0 para sair): "))
    
    # Verifica se é para encerrar o programa
    if numero == 0:
        print("Programa encerrado.")
        break
    
    # Adiciona o número à lista
    valores.append(numero)
    
    print("Lista (ordem de inserção):", valores)
    print("Lista (ordenada):", sorted(valores))
    
    
