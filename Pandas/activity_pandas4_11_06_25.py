import pandas as pd

df_filmes = pd.read_csv('Pandas/IMDB-Movie-Data.csv')


# 1. Verificar valores ausentes (NaN)
# --------------------------------------
print("Valores ausentes por coluna:")
print(df_filmes[['Revenue (Millions)', 'Metascore']].isnull().sum())


# 2. Criar df_filmes_completo removendo linhas com qualquer NaN
# --------------------------------------
df_filmes_completo = df_filmes.dropna()
print("\nQuantidade de linhas após remover ausentes:")
print(len(df_filmes_completo))
print(df_filmes_completo)


# 3. Criar df_filmes_preenchido_media
# Preencher valores ausentes com média e mediana
# --------------------------------------
df_filmes_preenchido_media = df_filmes.copy()

# Preencher 'Revenue (Millions)' com a média
media_revenue = df_filmes['Revenue (Millions)'].mean()
df_filmes_preenchido_media['Revenue (Millions)'].fillna(media_revenue, inplace=True)

# Preencher 'Metascore' com a mediana
mediana_metascore = df_filmes['Metascore'].median()
df_filmes_preenchido_media['Metascore'].fillna(mediana_metascore, inplace=True)

# Verificar se ainda há valores ausentes
print("\nValores ausentes após preenchimento:")
print(df_filmes_preenchido_media[['Revenue (Millions)', 'Metascore']].isnull().sum())

# Mostrar resultado final
print("\nDataFrame com valores preenchidos:")
print(df_filmes_preenchido_media)