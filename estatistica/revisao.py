import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

#1. Carregar dados
df = pd.read_csv('estatistica/notas.csv')
todas_notas = df.values.flatten()

# Medidas de Resumo
media = np.mean(todas_notas)
mediana = np.median(todas_notas)
moda = stats.mode(todas_notas, keepdims=True).mode[0]
media_aparada = stats.trim_mean(todas_notas, proportiontocut=0.1)

#Media simples por aluno
media_simples_alunos = df[['B1', 'B2', 'B3', 'B4']].mean(axis=1)
# Media Ponderada po aluno
pesos= [1, 2, 3, 4]
media_ponderada_alunos = (df['B1']*pesos[0] + df['B2']*pesos[1] + df['B3']*pesos[3] / sum(pesos))

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Média Simples por Aluno")
print(media_simples_alunos)
print("\n Média Ponderada po Aluno")
print(media_ponderada_alunos)