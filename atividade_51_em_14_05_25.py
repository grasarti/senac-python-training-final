# Criar um programa que:
# Continue pedindo uma senha até que ela:
# Tenha pelo menos 8 caracteres
# Tenha pelo menos uma letra maiuscula
# Tenha pelo menos uma letra minuscula
# Tenha pelo menos um numero

# import re

# while True:
#     senha = input( "Digite uma senha: ")
    
#     # verificações
#     if (len(senha) >= 8 and
#         re.search("[A-Z]", senha) and
#         re.search("[a-z]", senha) and
#         re.search("[0-9]", senha)):
        
#         print("Senha válida!")
#         break
#     else:
#         print("Senha inválida. Tente novamente!")
        
        
import re

while True:
    senha = input( "Digite uma senha: ")
    temMaiuscula = re.search("[A-Z]",senha)
    temMinuscula = re.search("[a-z]",senha)
    temNumero = re.search("[0-9]",senha)
    if len(senha) < 8:
        print("Senha precisa ter 8 caracteres")
    
    elif temMaiuscula == None:
        print(" 1 Letra maiúscula")
    
    elif temMinuscula == None:
        print(" 1 Letra minúscula")
        
    elif temNumero == None:
        print(" 1 Número")
        
    else:
        print("Senha compatível")
        break