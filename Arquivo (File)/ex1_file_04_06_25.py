# Ler um arquivo chamado frutas.csv que tem nomes de frutas e seus preços.
# • Criar uma função chamada frutas().
# • Essa função deve retornar um dicionário onde:
# • chave = nome da fruta
# • valor = preço da fruta (como float)

import csv

def frutas():
   dicionario_frutas = {}  # Criando um dicionário vazio
   
   try:
        with open("Arquivo (File)/frutas.csv") as arquivo:
            for linha in arquivo:
            # Remove espaços em branco e quebras de linha
                linha = linha.strip()
                if linha:
                    dados = linha.split(";")
                    dicionario_frutas[dados[0]] = float(dados[1])
     
   except FileNotFoundError:
       print("Arquivo 'frutas.csv' não encontrado.")
    
   except ValueError:
       print("Erro ao converter o preço para float.")                  

   return dicionario_frutas

# Testando a função
print(frutas())
