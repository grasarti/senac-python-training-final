# Um programa que:
# Tenha um saldo disponível (por exemplo, R$ 500)
# Peça ao usuário um valor para sacar 
# O valor precisa:
#     ser multiplo de 10
#     nao pode ultrapassar o saldo
# Se o valor for inválido, peça novamente
# Quando for válido, exiba o valor sacado e o saldo restante

saldo = 500 # saldo inicial

while True:
    saque = int(input("Digite o valor para sacar (múltiplo de 10): "))
    
    if saque % 10 != 0:
        print("Valor inválido! O valor deve ser múltiplo de 10.")
    elif saque > saldo:
        print("Saldo insuficiente!")
    else:
        saldo -= saque
        print(f"Saque realizado com sucesso! Valor sacado: R${saque}")
        print(f"Saldo restante: R${saldo}")
        break
    
