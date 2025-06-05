valorConta = float(input("Qual o valor da conta? "))

valorGorjeta = int(input("Qual o percentual da gorjeta? "))

totalGorjeta = (valorConta * valorGorjeta) / 100

totalConta = valorConta + totalGorjeta

print(f"O valor da gorjeta é de {totalGorjeta} e o valor da conta é {totalConta} ")