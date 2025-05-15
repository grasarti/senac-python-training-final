# peça uma string ao usuario dentro de um while
# imprima a string normalmente
# imprima uma linha de sublinhado (-) com o mesmo tamanho da string 
# o loop termina quando o usuario apenas pressiona Enter (string vazia)

while True:
    texto = input("Por favor, digite uma string: ")
    
    if texto == "":
        break
    
    print(texto)
    print("-" * len(texto)) # sublinha com a mesma quantidade de caracteres