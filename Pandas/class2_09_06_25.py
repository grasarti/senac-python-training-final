import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"

df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!")

# Head() e o Tail()

print("Primeiras 5 linhas do dataFrame de Filmes:")
print(df_filmes.head())

# Tail
print("\n Últimas 5 linhas do dataFrame de filmes:")
print(df_filmes.tail())

# Info
print("\n Informações sobre o DataFrame:")
print(df_filmes.info())

#Shape
print(f"\nO dataFrame de filmes tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}")

# Describe (gera estatística do dataframe)
print("Estatística descritiva do DataFrame:")
print(df_filmes.describe())

# Index (traz informações sobre os índices das linhas)
print("Informações do índice:")
print(df_filmes.index)

# Removendo linhas/colunas
# Criando uma cópia para não
df_sem_nan_linhas = df_filmes.copy()

# Removendo todas as linhas que contenham qualquer valor Nan (not a number/números ausentes ou inválidos)
df_sem_nan_linhas.dropna(inplace=True)
print(f"\n Número de linhas original: {len(df_filmes)}")
print(f"\n Número de linhas após drop: {len(df_sem_nan_linhas)}")

# Removendo colunas que tenham qualquer valor Nan
df_sem_nan_colunas = df_filmes.dropna(axis=1)
print(f"Colunas originais: {df_filmes.columns.tolist()}")
print(f"Colunas após dropna: {df_sem_nan_colunas.columns.tolist()}")

# Contando as frequências de coluna
contagem_diretores = df_filmes['Director'].value_counts()
print("\n Os 10 diretores mais frequentes: ")
print(contagem_diretores.head(10))

# Ordenando filmes pela nota (IMDB_Rating)
df_ordenado_por_nota = df_filmes.sort_values(by='IMDB_Rating', ascending=False)
print("\n Top 5 filmes por nota (IMDB_Ratting):")
print(df_ordenado_por_nota)

# Ordenando filmes por mais de uma coluna
df_ordenado_por_duas_colunas = df_filmes.sort_values(by= ['Released_Year', 'Gross'], ascending=[False, True])
print("\n Top 5 filmes por ano e gross:")
print(df_ordenado_por_duas_colunas.head())

# Converter caso necessário
df_filmes['Gross'] = df_filmes['Gross'].str.replace(',','')
df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')
df_filmes['IMDB_Rating'] = pd.to_numeric(df_filmes ['IMDB_Rating'], errors='coerce')

# Calculando a média de IMDB e Gross para cada Released_Year
metricas_por_ano = df_filmes.groupby('Released_Year').agg(
    Media_Rating=('IMDB_Rating','mean'),
    Media_Receita=('Gross','mean'),
    Total_filmes=('Series_Title','count'),
)
print(metricas_por_ano)

# Salvando em um arquivo csv sem o indice
df_filmes.to_csv('meus_filmes_bem_avaliados.csv', index=False)
print("\nDataframe salvo em 'Meus_filmes_bem_avaliados.csv")

