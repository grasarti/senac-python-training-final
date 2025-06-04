# Escrever um programa em Python que:
#   Abra o arquivo entrada.txt (supondo que ele já exista no mesmo local do seu código)
#   Leia todo o conteúdo do arquivo
#   Mostre esse conteúdo na tela (terminal)



# Abre o arquivo 'entrada.txt' no modo de leitura ("r" = read)
with open("Arquivo (File)/entrada.txt", "r", encoding="utf-8") as arquivo:
   conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo

# Exibe o conteúdo no terminal
print("Conteúdo do arquivo entrada.txt:\n")
print(conteudo)



# open("entrada.txt", "r"): abre o arquivo para leitura.
#   read(): lê todo o conteúdo de uma vez.
#   encoding="utf-8": garante que caracteres com acentos sejam lidos corretamente.
#   se o arquivo não existir, esse código vai gerar um erro. (Pode-se usar try/except se quiser tratar isso futuramente.)