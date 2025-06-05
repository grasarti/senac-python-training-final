# escreva uma função chamada add_filme(database:list, nome: str, diretor: str, ano: int, duracao: int)
# que adiciona um novo objeto de filme em um banco de dados de filmes

# o banco de dados é uma lista, e cada objeto de filme na lista é um dicionário

# o dicionário deve conter as seguintes chaves:
#     Nome 
#     diretor 
#     ano 
#     tempo de execução (duração)
# os valores dessas chaves são os argumentos fornecidos à função.


def add_filme(database:list, nome: str, diretor: str, ano: int, duracao: int):
    filme = {
        "nome": nome,
        "diretor": diretor,
        "ano": ano,
        "tempo de execução": duracao
    }
    database.append(filme)
    
meu_banco = []
add_filme(meu_banco, "Cidade de Deus", "Fernando Meirelles", 2002, 130)
print(meu_banco)