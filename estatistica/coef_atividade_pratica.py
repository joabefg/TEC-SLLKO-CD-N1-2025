import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Invest_Marketing': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Vendas_Mensais': [50, 55, 62, 68, 80, 85, 98, 105, 110, 125],
    'Horas_Treino': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    'Erros_Producao': [20, 18, 15, 16, 12, 10, 8, 9, 5, 4],
    'Idade_Imovel': [5, 50, 12, 35, 22, 40, 8, 15, 60, 2],
    'Preco_Venda': [300, 310, 290, 305, 315, 295, 300, 310, 305, 298]
    }
df = pd.DataFrame(data)

#Marketing vs Venda
matriz_corr = df[['Invest_Marketing', 'Vendas_Mensais']].corr()
print(matriz_corr)
matriz_corr2 = df[['Horas_Treino', 'Erros_Producao']].corr()
print(matriz_corr)
matriz_corr3 = df[['Idade_Imovel', 'Preco_Venda']].corr()
print(matriz_corr)

plt.figure(figsize=(14,12))

#HeatMap
plt.subplot(3, 2, 1)
sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Marketing vs Vendas')
plt.subplot(3, 2, 3)
sns.heatmap(matriz_corr2, annot=True, cmap='icefire', fmt=".2f")
plt.title('Treinamento vs Erros Operacionais')
plt.subplot(3, 2, 5)
sns.heatmap(matriz_corr3, annot=True, cmap='vlag', fmt=".2f")
plt.title("Idade Casas vs Preço")

#Dispersão
plt.subplot(3, 2, 2)
sns.scatterplot(x='Invest_Marketing', y='Vendas_Mensais', data=df, color='green')
plt.subplot(3, 2, 4)
sns.scatterplot(x='Horas_Treino', y='Erros_Producao', data=df, color='red')
plt.subplot(3, 2, 6)
sns.scatterplot(x='Idade_Imovel', y='Preco_Venda', data=df, color='blue')
plt.show()