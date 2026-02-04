import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from scipy import stats
import numpy as np

# 1. Carregar dados_________________________________________________________________________________________________
df = pd.read_csv('estatistica/notas.csv')
todas_notas = df.values.flatten()

# medidas de resumo_________________________________________________________________________________________________
media = np.mean(todas_notas)
mediana = np.median(todas_notas)
moda = stats.mode(todas_notas, keepdims=True).mode[0]
media_aparada = stats.trim_mean(todas_notas, proportiontocut=0.1)

# Média simples por aluno___________________________________________________________________________________________
media_simples_alunos = df[['B1', 'B2', 'B3', 'B4']].mean(axis=1)
# Média ponderada por aluno_________________________________________________________________________________________
pesos = [1, 2, 3, 4]
media_ponderada_alunos = (df['B1']*pesos[0] + 
                          df['B2']*pesos[1] + 
                          df['B3']*pesos[2] +
                          df['B4']*pesos[3] / 
                          sum(pesos))

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Media Aparada: {media_aparada:.2f}")
print("\n Média Simples por aluno")
print(media_simples_alunos)
print("\n Média Ponderada por aluno")
print(media_ponderada_alunos)

# Gráficos _________________________________________________________________________________________________________
plt.figure(figsize=(12,5))
# histograma________________________________________________________________________________________________________
plt.subplot(1, 2, 1)
sns.histplot(todas_notas, color='royalblue', alpha=0.7)
plt.xticks(np.arange(0,11,1))
plt.title("Histogramda de Frequência das Notas")
plt.xlabel('Notas')
plt.ylabel('Frequência')

# Boxplot___________________________________________________________________________________________________________
plt.subplot(1, 2, 2)
sns.boxplot(y=todas_notas, color='lightgreen')
plt.title('Boxplot das Notas(Quartis)')
plt.ylabel('Notas')

plt.show()