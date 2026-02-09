import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# 1. Lista de dados
dados = [50, 100, 115, 116, 118, 121, 121, 122, 124, 126, 129, 132, 135, 138, 142, 148, 154, 154, 158, 166, 175, 179, 210]

# 2. Quartis
Q1 = np.percentile(dados, 25)
Q2 = np.percentile(dados, 50)
Q3 = np.percentile(dados, 75)   
df_quantis = pd.DataFrame({
    'Quantis': ['Q1', 'Q2', 'Q3'],
    'Valores': [Q1, Q2, Q3]
})
print("Quartis das pressõe medidas:")
print(df_quantis)
print("\n")

#3. Limetes
iqr = Q3 - Q1
limite_inferior = Q1 - (1.5 * iqr)
limite_superior = Q3 + (1.5 * iqr)
df_limites = pd.DataFrame({
    'Limites': ['Limite Inferior', 'Limite Superior'],
    'Valores': [limite_inferior, limite_superior]
})
print("Limites das pressões medidas:")
print(df_limites)
print("\n")

# 4. outliers
outliers = [x for x in dados if x < limite_inferior or x > limite_superior]
print(f"Outliers encontrados {outliers} \n") 

# 5. Gráfico Boxplot
plt.figure(figsize=(8, 8))
plt.boxplot(dados)
plt.title("Gráfico de caixa das pressões")
plt.ylabel('Pressão sistólica (mmHg)')  
plt.grid(axis='y', linestyle='--', alpha=0.7)   
plt.show()
