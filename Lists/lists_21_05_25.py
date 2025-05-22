# Criar uma lista
minha_lista = [10,30,15]

# Acessando elementos por índice
print(minha_lista[0])
print(minha_lista[1])
print(minha_lista[2])

# Trabalhando com elementos da lista
resultado = minha_lista[0] + minha_lista[2]
print(resultado)

# tamanho da lista
tamanho_lista = len(minha_lista)
print(f"Minha lista tem {tamanho_lista} de tamanho")

# Remove o valor de um elemento de uma lista
numeros.remove(50)
numeros.insert(10,"Graci")

numeros.remove("Graci")

#Sort - Classificação
lista = [0,45,68,98,78,65,23,35,54,47,89]
lista.sort()
#Sorted cria uma cópia da lista original em outra variavel
lista_v2 = sorted(lista)
 
print(lista_v2)
print(lista)

# Máximo, Mínimo, Soma
Lista_numeros = [0,45,78,6,32,15]
print(max(Lista_numeros))
print(min(Lista_numeros))
print(sum(Lista_numeros))

lista_mediana = [15,48,79,36,56,89,74,15,32]

def mediana(minha_lista: list):
    ordenada = sorted(minha_lista)
    centro_lista = len(ordenada) // 2
    return ordenada[centro_lista]

print(f"A mediana é {mediana(lista_mediana)}")