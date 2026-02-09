import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1. Importar dados
df = pd.read_csv('estatistica/funcionarios.csv')

#2. Definir padrão do grafico
plt.figure(figsize=(22,6))

#3. Cáulculos e subplot
analises = {}
#3.1 Amplitude salarial
analises['1. Amplitude Salarial'] = df['Salario'].max() - df['Salario'].min()
media_salario= df['Salario'].mean()
desvio_salario= df['Salario'].std()
plt.subplot(1, 6, 1)
plt.title('Salarios')
sns.stripplot(x=df['Salario'], jitter=True, color='skyblue')
plt.axvline(media_salario, color='red')
plt.axvline(media_salario - desvio_salario, color='gray')

#3.2
analises['2. Desvio Padrão Performace'] = df['Nota_Performance'].std()
media_performace =  df['Nota_Performance'].mean()
desvio_performace= df['Nota_Performance'].std()
plt.subplot(1, 6, 2)
plt.title('Performace')
sns.stripplot(x=df['Nota_Performance'], jitter=True, color='olive')
plt.axvline(media_performace, color='red')
plt.axvline(media_performace - desvio_performace, color='gray')
#4. Imprimir valores
for caso, valor in analises.items():
    print(f"{caso}: {valor:.2f}")

#5. Exibir o grafico
plt.tight_layout(rect=[0, 0.3, 1, 0.95])
plt.show()