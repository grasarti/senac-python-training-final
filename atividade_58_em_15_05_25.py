# peça uma palavra ao usuário
# crie um quadro com 30 caracteres de largura
# a palavra deve aparecer centralizada, preenchendo o resto com * dos dois lados

texto = input("Digite uma palavra ou frase: ")
#largura total
largura_total = 30
#Linhas do topo e do rodapé
linha_borda = "*" * largura_total
#aqui é o espaço total disponivel tirando o tamanho da palavra
espacos_total = largura_total - len(texto)
#aqui é quanto de espaço para esquerda que é o espaco_total dividido por 2
espacos_esquerda = espacos_total // 2 
#aqui é o espaço da direita
espacos_direita = espacos_total - espacos_esquerda-2
#aqui monta a linha central

if len(texto) % 2 == 0:    
    linha_central = "*" + " " * espacos_esquerda + texto + " " * espacos_direita + "*"
else:
    linha_central = "*"+ texto + "*"


print(linha_borda)
print(linha_central)
print(linha_borda)
