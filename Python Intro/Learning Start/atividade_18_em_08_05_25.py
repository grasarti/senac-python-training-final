numero = int(input("Por favor digite um número: "))
if numero < 1000:
    print("Este número é menor que 1000. Obrigado!")
elif numero < 1000 and numero < 100:
    print("Este número é menor que 1000. Este número é menor que 100. Obrigado!")
elif numero < 1000 and numero < 10:
    print("Este número é menor que 1000. Este número é menor que 100. Este número é menor que 10. Obrigado!")
else:
    input("Por favor digite um número: ")
    print("Obrigado!")