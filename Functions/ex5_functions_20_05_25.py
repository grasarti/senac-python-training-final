# definir a função
def Repetir(palavra, numero):
    #variavel que multiplica a string pelo numero passado como parametro
    stringTotal = (palavra * numero)
    # variavel que inicia em zero para posteriormente ser usado como controle
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