
def adicionar_entrada_diario():
    data = input("Digite a data (ex: 05/06/2025): ")
    descricao = input("Digite o que aconteceu hoje: ")
    
    # cria o texto da entrada
    entrada = f"Data: {data} - Descrição: {descricao}\n"
    
    #abre o arquivo e adiciona a entrada
    with open ("Arquivo (File)/diario.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(entrada)
        
    print("Entrada salva com sucesso!")

# chamar a função
adicionar_entrada_diario()

# não usei dicionário - só texto simples
# o usuário digita a data manualmente


