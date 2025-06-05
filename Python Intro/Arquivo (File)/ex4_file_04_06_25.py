# Ler um arquivo chamado texto.txt
# Contar quantas linhas ele possui
# Exibir o total de linhas no final


# Abre o arquivo 'texto.txt' no modo leitura
with open("Arquivo (File)/texto.txt", "r", encoding="utf-8") as arquivo:
   linhas = arquivo.readlines()  # Lê todas as linhas e salva em uma lista

# Conta o número de linhas
quantidade_linhas = len(linhas)

# Exibe o resultado
print(f"\n O arquivo contém {quantidade_linhas} linhas.\n")



# readlines() → lê o arquivo linha por linha e armazena tudo em uma lista.
# len(linhas) → conta o total de itens (linhas) dessa lista.
# O f"" serve para montar a frase com o valor da variável dentro