# salario_por_hora = float(input("Digite o salário por hora: "))
# horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
# dia_da_semana = input("Digite o dia da semana: ")

# #verifica se é domingo
# if salario_por_hora == "domingo":
#     salario_por_hora *= 2 #dobra o valor
    
# #calcula o salário diário
# salario_diario = salario_por_hora * horas_trabalhadas

# #exibe o resultado
# print(f"O salário do dia é: R${salario_diario:.2f}")


salario_hora = float(input("Digite o salário por hora: "))
horas_trabalhadas = float(input("Digite as horas trabalhadas: "))
dia_semana = input("Digite o dia da semana: ")

if dia_semana == "domingo":
    salario_dia = (salario_hora * 2) * horas_trabalhadas
else:
    salario_dia = salario_hora * horas_trabalhadas
    
print(f"Salário diário: R$ {salario_dia:.2f}")