import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#1. lista de dados
dados = [50, 100, 115, 116, 118, 
         121, 121, 122, 124, 126,
         129, 132, 135, 138, 142,
         148, 154, 154, 158, 166,
         175, 179, 210]

#2. quartis
q1 = np.percentile(dados, 25)
q2 = np.percentile(dados, 50)
q3 = np.percentile(dados, 75)
df_quartis = pd.DataFrame({
    'Quartil': ['Q1', 'Q2', 'Q3'],
    'Valor': [q1, q2, q3]
})
print("quartis das pressoes medidas:")
print(df_quartis)
print("\n")

#3. limites
iqr = q3 - q1
limite_inferior = q1 - ( 1.5 * iqr)
limite_supeior = q3 + (1.5 * iqr)
df_limites = pd.DataFrame({
    'Limites': ['Inferior', 'Superior'],
    'Valor': [limite_inferior, limite_supeior]
})
print("Limites das pressões medidas:")
print(df_limites)
print("\n")

#4. outliers
outlies = [x for x in dados if x < limite_inferior or x > limite_supeior]
print( f"Outliers encontrados {outlies} \n")

#5. boxplot
plt.figure(figsize=(8, 8))
plt.boxplot(dados)
plt.title("grafico de caixa das pressões")
plt.ylabel('pressão sistolica (mmHg)')
plt.xticks([])
plt.grid(axis='y', linestyle = '--', alpha=0.7)
plt.show()