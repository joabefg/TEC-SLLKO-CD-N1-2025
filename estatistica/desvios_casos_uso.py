import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1. Importar dados
df = pd.read_csv('estatistica/funcionarios.csv')

#2. Definir o gráfico
plt.figure(figsize=(22,6))

#3. Cálculos e Subplot
analises = {}
#3.1 Amplitude Salarial
analises['1. Amplitude Salarial'] = df['Salario'].max() - df['Salario'].min()
media_salarios = df['Salario'].mean()
desvio_salarios = df['Salario'].std()
plt.subplot(1, 6, 1)
plt.title('Salários')
sns.stripplot(x=df['Salario'], jitter=True, color='Skyblue')
plt.axvline(media_salarios, color='red')
plt.axvline(media_salarios - desvio_salarios, color='gray')
#3.2 Desvio padrão performance
analises['2. Desvio Padrão Performance'] = df['Nota_Performance'].std()
media_performance = df['Nota_Performance'].mean()
desvio_performance= df['Nota_Performance'].std()
plt.subplot(1, 6, 2)
plt.title('Performance')
sns.stripplot(x=df['Nota_Performance'], jitter=True, color='olive')
#4. Imprimir os valores
for caso, valor in analises.items():
    print(f"{caso}: {valor:.2f}")

#5. Exibir o gráfico
plt.tight_layout(rect=[0, 0.3, 1, 0.095])
plt.show()