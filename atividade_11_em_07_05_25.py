capital = int(input("\n Qual o capital inicial? "))
taxaJuros = int(input("\n Qual é a taxa de juros anual? "))
anos = int(input("\n Quanto anos? "))
juros = capital * (taxaJuros / 100) * anos
montante = capital + juros

print(f"\n Jurus simples: {montante} \n")