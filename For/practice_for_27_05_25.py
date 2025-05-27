# peça ao usuário uma string (como "Python")
# imprima cada letrada string em uma linha separada, com um * logo depois

texto = input("Digite uma palavra: ")
for letra in texto:
    print(letra + "*")


# outra forma de executar

texto = input("Digite uma palavra: ")
for letra in texto:
    print(letra,end="*")