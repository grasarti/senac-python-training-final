while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou: {numero}")
        break

    except ValueError:
        print("Erro: Isso não é um número inteiro!Tente novamente!")
    
    