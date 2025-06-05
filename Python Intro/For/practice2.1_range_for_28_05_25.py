# escrever uma função chamada mais_caracteres, que recebe um argumento string 
# a função retorna o caractere que tem mais ocorrências dentro da string 


def mais_caracteres(texto):
    contagem = {}       # dicionário para contar quantas vezes cada caractere aparece
    ordem = []          # lista para guardar a ordem de aparição dos caracteres
    
    for char in texto:
        if char not in contagem:
            contagem[char] = 1      # se o caractere ainda não foi contado, inicia com 1
            ordem.append(char)      # salva a ordem em que apareceu
        else:
            contagem[char] += 1     # se já foi contado, soma mais 1
    
    maior_qtd = max(contagem.values())      # pega o maior valor de ocorrência
    
    for char in ordem:
        if contagem[char] == maior_qtd:
            return char         # retorna o primeiro caractere com maior ocorrência


# exemplo:
print(mais_caracteres("abacate"))       #saída: 'a'
print(mais_caracteres("chocolate"))       #saída: 'c'