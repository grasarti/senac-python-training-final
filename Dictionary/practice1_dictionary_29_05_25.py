# criar uma função chamada histogram que receba uma string e imprima quantas vezes
# cada letra aparece, usando asteriscos(*) para representar as repetições


def histogram(texto):
    # cria um dicionário para contar as letras
    contagem = {}
    
    # conta quantas vezes cada letra aparece
    for letra in texto:
        if letra in contagem:
            contagem[letra] += 1        # se já existir, soma 1
        else:
            contagem[letra] = 1         # se for a primeira vez, inicia com 1
    
    # imprime o histograma
    for letra in sorted(contagem):      # ordena as letras para manter a saída organizada
        print(letra, "*" * contagem[letra])         # ex: b *** se tiver 3 vezes
        
# exemplo

histogram("banana")

# usa um dicionário para guardar quantas vezes cada letra aparece
# depois usa print(letra, "*" * quantidade) para desenhar os asteriscos
# sorted() usa só para deixar a saída em ordem alfabética(opcional)