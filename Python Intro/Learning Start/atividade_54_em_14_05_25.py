# Um programa que:
# Peça ao usuário para digitar duas palavras
# Continue pedindo enquanto elas não tiverem o mesmo número de caracteres
# Quando tiverem, exiba uma mensagem de sucesso

while True:
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    
    if len(palavra1) == len(palavra2):
        print("As palavras têm o mesmo número de caracteres!")
        break
    else:
        print("As palavras têm tamanhos diferentes. Tente novamente! \n")
        
        