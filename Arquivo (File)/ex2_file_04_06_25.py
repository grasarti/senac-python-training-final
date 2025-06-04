# Pede para o usuário digitar um texto
texto = input("Digite um texto para salvar no arquivo: ")

# Abre (ou cria) o arquivo 'saida.txt' no modo de escrita ("w" = write)
with open("saida.txt", "w", encoding="utf-8") as arquivo:
   arquivo.write(texto)  # Escreve o texto no arquivo
print("Texto salvo com sucesso no arquivo 'saida.txt'!")