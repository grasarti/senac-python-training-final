import pandas as pd

url_filmes = "Pandas/IMDB-Movie-Data.csv"
 
df = pd.read_csv(url_filmes)

# Contar quantos filmes cada diretor dirigiu (Director) e mostrar os 5 mais frequentes
top_diretores = df['Director'].value_counts().head(5)
print(top_diretores)

# Ordenar os filmes por tempo de duração (Runtime) em ordem decrescente e mostrar os 10 mais longos
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')
mais_longos = df.sort_values(by='Runtime', ascending=False).head(10)
print(mais_longos[['Series_Title', 'Runtime']])

# Ordenar por Certificate (alfabética) e depois por Meta_score (decrescente). Mostrar os 5 primeiros
df['Meta_score'] = pd.to_numeric(df['Meta_score'], errors='coerce')
ordenado = df.sort_values(by=['Certificate', 'Meta_score'], ascending=[True, False])
print(ordenado[['Series_Title', 'Certificate', 'Meta_score']].head(5))

# Converter Meta_score e Runtime para numérico (tratando erros)
df['Meta_score'] = pd.to_numeric(df['Meta_score'], errors='coerce')
df['Runtime'] = pd.to_numeric(df['Runtime'], errors='coerce')

# Agrupar pro Certificate, calculando:
agrupado = df.groupby('Certificate').agg(
    media_runtime=('Runtime', 'mean'),
    media_metascore=('Meta_score', 'mean'),
    total_filmes=('Series_Title', 'count'),
).reset_index()

print(agrupado)