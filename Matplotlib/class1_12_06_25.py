import matplotlib.pyplot as plt
import numpy as np

# Gráfico de Linha
x2 = [1,2,3,5,6]
y = [2,5,6,8,6]

plt.plot(x2,y)
plt.title('Exemplo de linha')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()

# Gráfico de Barra
categorias = ['A','B','C']
valores = [10,2,30]

plt.bar(categorias,valores)
plt.title('Barras')
plt.show()

# Gráfico de pizza

plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Pizza')
plt.show()

# Histograma
dados = np.random.randn(1000)
plt.hist(dados,bins=30)
plt.title('Histograma')
plt.show()

# Dispersão
x = np.random.rand(50)
y = x + np.random.randn(50)*0.1
plt.scatter(x,y)
plt.title('Dispersão')
plt.show()

