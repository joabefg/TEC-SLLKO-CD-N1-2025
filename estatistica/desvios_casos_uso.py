import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt
import seaborn as sns

#1. carregar dados
df = pd.read_csv('estatistica/funcionarios.csv')

#2. definir grafico
plt.figure(figsize=(22, 6))

#3. calculos e subplots
analises = {}
#3.1 amplitude salarial
analises['1. Amplitude Salarial'] = df['Salario'].max() - df['Salario'].min()
media_salarios = df['Salario'].mean()
desvio_salario = df['Salario'].std()
plt.subplot(1, 5, 1)
plt.title('Salários')
sns.stripplot(x=df['Salario'], jitter=True, color='skyblue')
plt.axvline(media_salarios, color='red' )
plt.axvline(media_salarios - desvio_salario, color='gray')
#3.2 desvio padrao performance
analises['2. Desvio Padrão Performance'] = df['Nota_Performance'].std()
media_performance = df['Nota_Performance'].mean()
desvio_performance = df['Nota_Performance'].std()
plt.subplot(1, 5, 2)
plt.title('Performance')
sns.stripplot(x=df['Nota_Performance'], jitter=True, color='olive')
plt.axvline(media_performance, color='red')
plt.axvline(media_performance - desvio_performance, color='gray')
#3.3 DAH Engajemento
analises['3. DAH Engajamento'] = (df['Engajamento'] - df['Engajamento'].mean()).abs().mean()
media_engajamento = df['Engajamento'].mean()
desvio_engajamento = df['Engajamento'].std()
plt.subplot(1, 5, 3)
plt.title('CLima organizacional')
sns.stripplot(x=df['Engajamento'], jitter=True, color='gold')
plt.axvline(media_engajamento, color='red')
plt.axvline(media_engajamento - desvio_engajamento, color='gray')
#3.4 variancia meses p promoção
analises['4. Variância das promoções'] = df['Meses_ate_Promocao'].var()
media_promocao = df['Meses_ate_Promocao'].mean()
desvio_promocao = df['Meses_ate_Promocao'].std()
plt.subplot(1, 5, 4)
plt.title('Meritocracia Promoções')
sns.stripplot(x=df['Meses_ate_Promocao'], jitter=True, color='teal')
plt.axvline(media_promocao, color='red')
plt.axvline(media_promocao - desvio_promocao, color='gray')
#3.5 Amplitude custo de Saúde
analises['5. Amplitude Custo Saúde'] = df['Custo_Saude_Anual'].max() - df['Custo_Saude_Anual'].var()
media_saude = df['Custo_Saude_Anual'].mean()
desvio_saude = df['Custo_Saude_Anual'].std()
plt.subplot(1, 5, 5)
plt.title('Risco Atuarial')
sns.stripplot(x=df['Custo_Saude_Anual'], jitter=True, color='coral')
plt.axvline(media_saude, color='red')
plt.axvline(media_saude - desvio_saude, color='gray')


#4. imprimir os valores
for caso, valor in analises.items():
    print(f"{caso}: {valor:.2f}")

#5. exebir grafico
plt.tight_layout(rect=(0, 0.3, 1, 0.95))
plt.show()