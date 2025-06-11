import pandas as pd

# Exemplo de dados fictícios - prática
dados = {
   'Title': ['Filme A', 'Filme B', 'Filme C', 'Filme D', 'Filme E', 'Filme F'],
   'Rating': [8.2, 7.5, 9.0, 6.8, 7.0, 8.5],
   'Metascore': [82, 75, 90, 70, 65, 88],
   'Description': ['desc A', 'desc B', 'desc C', 'desc D', 'desc E', 'desc F'],
   'Votes': [12000, 8500, 30000, 15000, 9000, 25000]
}

df_filmes = pd.DataFrame(dados)

df_filmes['Rating_Metascore_Diff'] = abs(df_filmes['Rating'] - (df_filmes['Metascore'] / 10))

print(df_filmes[['Title', 'Rating', 'Metascore', 'Rating_Metascore_Diff']].head(5))

df_sem_description = df_filmes.drop(columns=['Description'])

df_filmes.rename(columns={'Votes': 'Numero_Votos'}, inplace=True)

print(df_filmes.columns)

