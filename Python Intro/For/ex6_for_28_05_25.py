# escreva uma função chamada sem_vogal, que receba um argumento string 
# a função retorna uma nova string, que deve ser a mesma que a original, mas com todas as vogais removidas
# é possível assumir que a sequência conterá apenas caracteres do alfabeto inglês minúsculo de a - z


def sem_vogal(texto):
    vogais = 'aeiou'        # lista das vogais a serem removidas
    resultado = ''          # string vazia para guardar os caracteres sem vogais 
    
    for letra in texto:
        if letra not in vogais:     # se não for vogal, adiciona ao resultado
            resultado += letra
            
    return resultado        # retorna a string final sem vogais

# exemplo de uso
print(sem_vogal("programacao"))       # saída: 'prgrmc'



# explicação
# entrada: "programacao"
# remove vogais: 'o', 'a', 'a', 'o'
# resultado: "prgrmc"