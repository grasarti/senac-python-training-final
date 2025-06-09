import pandas as pd

url_filmes = "Pandas/netflix_titles.csv"

df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!")

# Head
print("Primeiras 7 linhas do dataFrame de Filmes:")
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