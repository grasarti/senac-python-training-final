salario = int(input("Qual o seu salário?"))

horasMes = int(input("Quantas horas trabalha no mês?"))

valorHora = salario / horasMes

dia = 8

porDia = valorHora * dia

print(f"O funcionário ganha: R$ {valorHora} por hora")
print(f"Por dia ele ganha: R$ {porDia}")