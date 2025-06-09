
import pandas as pd

# criando uma série
idade = pd.Series([1,2,3,4,5,6])
print(idade)

idades_nomes = pd.Series([1,2,3,4],index=['Ana','João','Maria','Carlos'])
print(idades_nomes)

# Data Frames
dados_alunos = {
    'nome':['Ana','João','Maria','Carlos'],
    'idade':[1,2,3,5],
    'Curso':['Engenharia','Medicina','Direito','Engenharia']
}

df_alunos = pd.DataFrame(dados_alunos)
print(df_alunos)
