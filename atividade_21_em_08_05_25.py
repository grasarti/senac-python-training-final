temp_fahrenheit = int(input("Digite os Graus em Fahrenheit:"))
c = (temp_fahrenheit - 32) * (5 / 9)

if c < 0:
    print(f"{c} - Brrrrr!!! Está frio!!!")
else:
    print(f"{c} Ta safe!")