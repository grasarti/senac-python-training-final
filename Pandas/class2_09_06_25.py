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

