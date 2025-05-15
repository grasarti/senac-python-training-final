dadosNome = "Graci"

nome = input("Digite seu nome: ")
cidade = "Curitiba"
estado = "PR"
cep = "81550-110"

if nome == dadosNome:
    print(f"Nome: {nome} \n Cidade: {cidade} \n Estado: {estado} \n cep: {cep}")
else:
    print("Esse usuário não está em nossas base de dados.")