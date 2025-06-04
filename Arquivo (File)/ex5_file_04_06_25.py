# Ler um arquivo dados.csv que tem nome e idade separados por vírgula
# Criar um novo arquivo chamado dados_maiores.csv
#     com apenas as pessoas com 18 anos ou mais


with open("Arquivo (File)/dados.csv", "r", encoding="utf-8") as entrada:
   with open("dados_maiores.csv", "w", encoding="utf-8") as saida:
       cabecalho = next(entrada)         # Lê e guarda o cabeçalho
       saida.write(cabecalho)            # Escreve o cabeçalho no novo arquivo
       for linha in entrada:
           linha = linha.strip()
           nome, idade = linha.split(",")
           if int(idade) >= 18:
               saida.write(linha + "\n")
               
  
           
# strip() remove espaços e \n no final das linhas.
# split(",") separa os valores da linha.
# int(idade) converte o valor da idade para número inteiro.
# write() grava a linha no novo arquivo.