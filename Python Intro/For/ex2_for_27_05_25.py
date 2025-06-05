# escrever uma função chamada anagramas, que:
#     recebe 2 strings como argumento
#     retorna True se forem anagramas uma da outra (ou seja se tem exatamente as mesmas letras)
#     da para usar a função sorted () para facilitar
    
def anagramas(a, b):
    return sorted(a) == sorted(b)

print(anagramas("tame", "meta"))
print(anagramas("python", "java"))

