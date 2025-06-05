with open("dados.txt") as arquivo:
    f = arquivo.read()
    print(f)

import os

os.remove("dados2.txt")
if os.path.exists("atividades/apagar"): # path = pasta
    print("Sim, a pasta existe")
    os.rmdir("atividades/apagar") # apaga pasta
else:
    print("Pasta não existe")
    os.mkdir("atividades/apagar") # cria pasta
    
    