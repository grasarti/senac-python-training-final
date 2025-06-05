# criar uma função que peça ao usuário para cadastrar 5 senhas
# cada senha deve ter pelo menos 8 caracteres e conter um numero
# senhas inválidas devem ser rejeitadas com mensagem de erro 
# ao final, imprimir todas as senhas inválidas

senhas = []
while len(senhas) < 5:
        senha = input("Digite uma senha (mínimo 8 letras e com um número): ")
        
        # verifica se a senha tem pelo menos 8 caracteres
        if len(senha) < 8:
            print("Senha muito curta! Tente novamente.")
            continue
        
        # verifica se tem pelo menos um número
        tem_numero = False
        for letra in senha:
            if letra.isdigit():
                tem_numero = True
                break
            
        if not tem_numero:
            print("A senha precisa ter pelo menos um número. Tente novamente!")
            continue
        
        # se passou pelas verificações, adiciona na lista
        senhas.append(senha)
        print("Senha cadastrada com sucesso!\n")

print("Senhas cadastradas:")
for s in senhas:
    print(s)
    
    
# outra forma de executar
# import re

# def cadastrar_senhas():
#     senhas = []
# while len(senhas) < 5:
#     senha = input(f"Digite a {len(senhas)+1}ª senha: ")

# if len(senha) >= 8 and re.search("[0-9]", senha) |- None:
#     senhas.append (senha)
# else:
#     print("Senha inválida! Deve ter pelo menos 8 caracteres E conter um número.")

# print ("Senhas válidas:")

# i = 0
# while i < len (senhas):
#     print (senhas [1])
#     i += 1
# cadastrar_senhas()