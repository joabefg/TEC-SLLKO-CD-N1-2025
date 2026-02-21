import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = {
    'Maquina_A': [28, 30, 31, 29, 30, 32, 27, 30, 31, 32],
    'Maquina_B': [30, 20, 40, 30, 35, 25, 30, 15, 45, 30]
}

df = pd.DataFrame(dados)

media = df.mean()
mediana = df.median()
variancia = df.var()
desvio_padrao = df.std()
correlacao = df['Maquina_A'].corr(df['Maquina_B'])

print("=== RESULTADOS ===\n")

print("Média:")
print(media, "\n")

print("Mediana:")
print(mediana, "\n")

print("Variância:")
print(variancia, "\n")

print("Desvio Padrão:")
print(desvio_padrao, "\n")

print("Coeficiente de Correlação:")
print(correlacao)

plt.figure()
plt.scatter(df['Maquina_A'], df['Maquina_B'])
plt.title("Gráfico de Dispersão - Máquina A vs Máquina B")
plt.xlabel("Maquina_A")
plt.ylabel("Maquina_B")
plt.show()

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.title("Heatmap de Correlação")
plt.show()