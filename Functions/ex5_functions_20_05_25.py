def Repetir(palavra, numero):
    stringTotal = (palavra * numero)
    linha = 0
    while linha < numero:
        coluna = 0
        letras = " "
        while coluna < numero:
            posicao = linha * numero + coluna
            letras += stringTotal[posicao]
            coluna += 1
        print(letras)
        linha += 1

Repetir("Jumanji",4)