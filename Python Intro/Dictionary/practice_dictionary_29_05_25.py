# lista para dicionário

lista_palavras = [
  "banana", "leite", "cerveja", "queijo", "leite azedo", "suco", "linguiça",
  "tomate", "pepino", "manteiga", "margarina", "queijo", "linguiça",
  "cerveja", "leite azedo", "leite azedo", "manteiga", "cerveja", "chocolate"
] 

def contagens(minha_lista):
    palavras = {} # "chave":"valor"
    for palavra in minha_lista:
        if palavra not in palavras:
            palavras[palavra] = 0
        palavras[palavra] += 1
    return palavras

print(contagens(lista_palavras))