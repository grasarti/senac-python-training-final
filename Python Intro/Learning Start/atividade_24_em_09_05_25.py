# entrada de dados
temperatura = int(input("Qual é a previsão do tempo para amanhã? Temperatura: "))
vai_chover = input("Vai chover (sim/não): ")

#sugestão de roupas com base na temperatura
if temperatura > 20:
    sugestao = "Use jeans e uma camiseta!"
elif temperatura >= 10:
    sugestao = "Use jeans e uma camiseta. Recomendo um suéter também!"
else:
    sugestao = "Use um casaco pesado, calça e cachecol!"

# se vai chover adicionar guarda-chuva
if vai_chover == "sim":
    sugestao += ". E não esqueça o guarda-chuva também!"

# exibir resultado
print(sugestao)



# graus = int(input("Digite a temperatura: "))
# chuva = int(input("Var chover? 0 - Não, 1 - Sim: "))

# if graus > 20:
#     if chuva == 0:
#         print("Use jeans e camiseta")
#     else:
#         print("Use jeans e camiseta mas leve um Guarda Chuva")
    
# elif graus >= 10 and graus < 20:
#     if chuva == 0:
#         print("Use jeans e camiseta e leve um suéter")
#     else:
#         print("Use jeans e camiseta e leve um suéter. Leve Guarda-Chuva")
        
# elif graus >= 5 and graus < 10:
#     if chuva == 0:
#         print("Eta Pega!! Frio da peste! Não saia de casa")
#     else:
#         print("Não saia! Frio do Djanho e Muita chuva")
# else:
#     print("Nem pense! Durma")