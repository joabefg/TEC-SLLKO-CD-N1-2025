import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('estatistica/dados_estudantes.csv', sep=';', decimal='.', encoding='utf-8-sig')

# Definir a Figura do Gráfico
plt.figure(figsize=(22,6))

# Caso 1: Quintis - Top 20% maiores gastos na cantina
corte_q5 = df['Gastos'].quantile(0.80)
print(f"TOP 20% CLIENTES CANTINA - Corte: > {corte_q5:.2f}")
print(df[df['Gastos'] >= corte_q5][['Matricula', 'Nome', 'Gastos']].to_string())
plt.subplot(1, 6, 1)
plt.title('Gastos na Cantina')
plt.ylabel('Valor (R$)')
sns.boxplot(y=df['Gastos'], color='skyblue')

# Caso 2: Quartis - Outliers de Valor de bolsas
Q1, Q3 = df['Bolsas_Valor'].quantile([0.25, 0.75])
IQR =  Q3 - Q1
limite_sup = Q3 + 1.5 * IQR
print(f'2. OUTLIERS DE BOLSAS (Corte: > {limite_sup:.2f})')
print (df[df['Bolsas_Valor'] > limite_sup][['Matricula', 'Nome', 'Bolsas_Valor']].to_string(index=False))
plt.subplot(1, 6, 2)
plt.title('Desconto na Bolsa de Estudos')
plt.ylabel('Bolsa (%)')
sns.boxplot(y=df['Bolsas_Valor'], color='olive')

#  Caso 3: Decis - 10% Melhores Notas (9o Decil)
corte_d9 = df['Notas'].quantile(0.90)
print(f'3. ALUNOS COM BOLSA (Corte: > {corte_d9:.2f})')
print(df[df['Notas'] >= corte_d9][['Matricula', 'Nome', 'Notas']].to_string(index=False))
plt.subplot(1, 6, 3)
plt.title('Notas dos Alunos')
plt.ylabel('Notas')
sns.boxplot(y=df['Notas'], color='gold')

# Caso 4: Percentis - 5% Entregas mais demoradas (SLA)
CORTE_P95 = df['Tempo_Entrega_Dias'].quantile(0.95)
print(f"4. TEMPO DAS ENTREGAS (Corte: > {CORTE_P95:.2f})")
print(df[df['Tempo_Entrega_Dias'] >= CORTE_P95][['Matricula', 'Nome', 'Tempo_Entrega_Dias']].to_string(index=False))
plt.subplot(1, 6, 4)
plt.title('Tempo de Entrega')
plt.ylabel('Tempo (Dias)')
sns.boxplot(y=df['Tempo_Entrega_Dias'], color='salmon')

# Caso 5: Percentil 2,5 - Hemoglobina
corte_p2_5 = df['Hemoglobina'].quantile(0.025)
print(f'5. Suspeita de Anemia (Corte: < {corte_p2_5})')
print(df[df['Hemoglobina'] < corte_p2_5][['Matricula', 'Nome', 'Hemoglobina']].to_string(index=False))
plt.subplot(1,6,5)
plt.title('Taxa de hemoglobina no Sangue')
plt.ylabel('Hemoglobina (em uHb)')
sns.boxplot(y=df['Hemoglobina'], color='teal')

# Caso 6: Radiação (Curso de Radiologia - 75% maiores doses)
corte_p75 = df['Dose_Radiacao'].quantile(0.75)
print(f"6. Doses de Radiação (Corte: > {corte_p75:.2f})")
print(df[df['Dose_Radiacao'] >= corte_p75][['Matricula','Nome', 'Dose_Radiacao']].to_string(index=False))
plt.subplot(1, 6, 6)
plt.title('Dose de Radiação')
plt.ylabel('Radiação (uSv)')
sns.boxplot(y=df['Dose_Radiacao'], color='orchid')

plt.tight_layout(rect=[0, 0.3, 1, 0.95])
plt.show()