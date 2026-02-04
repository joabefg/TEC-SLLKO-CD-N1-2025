import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# 1. Carregar dados
df = pd.read_csv('estatistica/notas.csv')
todas_notas = df.values.flatten()

# Medidas de Resumo
media = np.mean(todas_notas)
mediana = np.median(todas_notas)
moda = stats.mode(todas_notas, keepdims=True).mode[0]
media_aparada = stats.trim_mean(todas_notas, proportiontocut=0.1)

# Media simples por aluno
media_simples_alunos = df[['B1', 'B2', 'B3', 'B4']].mean(axis=1)
# Media Ponderada por aluno
pesos= [1, 2, 3, 4]
media_ponderada_alunos = (df['B1']*pesos[0] + df['B2']*pesos[1] + 
                          df['B3']*pesos[2] + df['B4']*pesos[3] / sum(pesos))

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Media Aparada: {media_aparada:.2f}")
print("\n Média Simples por Aluno")
print(media_simples_alunos)
print("\n Média Ponderada por Aluno")
print(media_ponderada_alunos)

# Gráficos
plt.figure(figsize=(12, 5))
# Histograma - Tabela de Frequência
plt.subplot(1, 2, 1)
sns.histplot(todas_notas, color='royalblue', alpha=0.7)
plt.xticks(np.arange(0,11,1))
plt.title('Histograma de Frequências das Notas')
plt.xlabel('Nota')
plt.ylabel('Frenquência')

# Boxplot
plt.subplot(1, 2, 2)
sns.boxplot(y=todas_notas, color='lightgreen')
plt.title('Boxplot das Notas (Quartis)')
plt.ylabel('Notas')
plt.show()