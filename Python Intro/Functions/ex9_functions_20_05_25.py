# criar uma função chamada o_maior_numero, que:
# - recebe 3 argumentos numéricos;
# - retorna o maior valor entre os três;

def o_maior_numero(a, b, c):
    return max(a, b, c)

print(o_maior_numero(10, 6, 35))
print(o_maior_numero(4, 8, 5))

    
def o_maior_numero1(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

o_maior_numero1(50, 14, 69)