import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dados = {
    'Maquina_A': [28, 30, 31, 29, 30, 32, 27, 30, 31, 32],
    'Maquina_B': [30, 20, 40, 30, 35, 25, 30, 15, 45, 30]
}
df = pd.DataFrame(dados)

# Maquina A
media_A = df['Maquina_A'].mean()
mediana_A = df['Maquina_A'].median()
variancia_A = df['Maquina_A'].var()
desvio_padrao_A = df['Maquina_A'].std()
cv_A = (desvio_padrao_A / media_A) * 100
print(f"Maquina A: Média: {media_A} Mediana: {mediana_A} Variância: {variancia_A:.2f} Desvio Padrão: {desvio_padrao_A:.2f} coef. var.: {cv_A}")

# Maquina B
media_B = df['Maquina_B'].mean()
mediana_B= df['Maquina_B'].median()
variancia_B = df['Maquina_B'].var()
desvio_padrao_B= df['Maquina_B'].std()
cv_B = (desvio_padrao_A / media_A) * 100
print(f"Maquina B: Média: {media_B} Mediana: {mediana_B} Variância: {variancia_B:.2f} Desvio Padrão: {desvio_padrao_B:.2f} coef. var.: {cv_B}")

fig, (dispersao, heatmap) = plt.subplots(1, 2, figsize=(10, 5))
df.plot.scatter(x='Maquina_A', y='Maquina_B', ax = dispersao)
heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, ax=heatmap)
plt.show()
