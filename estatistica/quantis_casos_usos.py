import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('estatistica/dados_estudantes.csv', sep=';', decimal='.', encoding='utf-8-sig')

# Caso 1: Quintis - Top 20% maiores gastos na cantina_______________________________________________________________
corte_q5 = df['Gastos'].quantile(0.80)
print(f"TOP 20% CLIENTES CANTINA - Corte: > {corte_q5:.2f}")
print(df[df['Gastos'] >= corte_q5 ][['Matricula', 'Nome', 'Gastos']].to_string())

#  caso 2: Quartis - Outilers de Valor de Bolsas____________________________________________________________________
Q1, Q3 = df['Bolsas_Valor'].quantile([0.25, 0.75])
IQR = Q3 - Q1 
limite_sup = Q3 + 1.5 * IQR
print(f'2. OUTILIERS DE BOLSAS (Corte > {limite_sup:.2f})')
print(df[df['Bolsas_Valor'] > limite_sup][['Matricula', 'Nome', 'Bolsas_Valor']].to_string(index=False))