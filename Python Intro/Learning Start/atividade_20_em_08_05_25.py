numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Qual operação: (adicionar, multiplicar, subtrair, divisao)")

if operacao == "adicionar":
    resultado = numero1 + numero2
    print("Resultado:", resultado)
   
elif operacao == "multiplicar":
    resultado = numero1 * numero2
    print("Resultado:", resultado)
   
elif operacao == "subtrair":
    resultado = numero1 - numero2
    print("Resultado:", resultado)
   
elif operacao == "divisao":
    resultado = numero1 / numero2
    print("Resultado:", resultado)
