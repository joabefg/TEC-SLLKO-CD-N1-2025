import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

#1. carregar dados
df = pd.read_csv('estatistica/notas.csv')
todas_notas = df.values.flatten()

#medidas de resumo
media = np.mean(todas_notas)
mediana = np.median(todas_notas)
moda = stats.mode(todas_notas,keepdims=True).mode[0]
media_aparada = stats.trim_mean(todas_notas, proportiontocut=0.1)

#media simples por aluno
media_simples_alunos = df[['B1', 'B2', 'B3', 'B4']].mean(axis=1)
#media ponderada por aluno
peso = [1, 2, 3, 4]
media_ponderada_aluno = (df['B1']*peso[0] + df['B2']*peso[1] +
                          df['B3']*peso[2] + df['B4']*peso[3]/sum(peso))
print(f"Média: {media:.2f}")
print(f"Médiana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Média Aparada: {media_aparada:.2f}")
print("\n Média Simples por alunos")
print(media_simples_alunos)
print("\n Média ponderada por Aluno")
print(media_ponderada_aluno)

#Gradico
plt.figure(figsize=(12,5))
#histograma - tabela de frequencia
plt.subplot(1, 2, 1)
sns.histplot(todas_notas, color='royalblue', alpha=0.7)
plt.xticks(np.arange(0,11,1))
plt.title('Histograma de Frequencia de Notas')
plt.xlabel('Nota')
plt.ylabel('Frequencia')

#BOxplot
plt.subplot(1, 2, 3)
