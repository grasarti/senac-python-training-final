# A atividade exibida pede para criar uma função em Python chamada mesmo_caracter,
# que recebe uma string e dois inteiros como argumentos (esses inteiros são índices).
# A função deve retornar:
#     - True se os caracteres nos índices forem iguais;
#     - False se forem diferentes ou se algum dos índices estiver fora do alcance da string 

def mesmo_caracter(texto, indice1, indice2):
    # verifica se os índices estão dentro dos limites da string
    if 0 <= indice1 < len(texto) and 0 <= indice2 < len(texto):
        return texto[indice1] == texto[indice2]
    else:
        return False

print(mesmo_caracter("python", 0, 1))
print(mesmo_caracter("python", 0, 6))
print(mesmo_caracter("python", 0, 0))
print(mesmo_caracter("marcelo", 1, 10))
print(f"{mesmo_caracter("arara", 0, 4)}\n")


# outra forma de executar:

def mesmo_caracter(texto, i, j):
    if i < 0 or j < 0 or i >= len(texto) or j >= len(texto):
        return False
    else:
        if texto[i] != texto[j]:
            return False
        else:
            return True

print(mesmo_caracter("Marcelinha", 1, 9))
print(mesmo_caracter("Marcelinha", -1, 9))