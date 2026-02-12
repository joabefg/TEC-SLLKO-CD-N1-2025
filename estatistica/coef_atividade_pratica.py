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

# Marketing vs venda
matriz_corr = df[['Invest_Marketing','Vendas_mensais']].corr()
print(matriz_corr)