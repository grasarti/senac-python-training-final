# for
lista = ["Maria", "Madalena", "Pedro", "Paulo", "Alex", "1"]
for nome in lista:
    print(nome)
    if len(nome) > 2:
        print(f"O {nome} tem mais de 2 caracteres")
    else:
        print(f"{nome} tem menos de 2 caracteres")


# range no for
# aqui com 1 argumento são quantas interações quero que o código execute

for i in range(5,20):
    print(i)
    

# repete o bloco de código pulando de 2 em 2

for j in range(0,10,2):
    print(j)
    

# criando uma lista a partir do Range

numero = list(range(3,15))
print(numero)
print(numero[5])

for i in numero:
    print(i)