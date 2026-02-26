import pandas as pd

df = pd.read_csv("ferramentas analise/analise_negocios.csv")

# ANÁLISE FINANCEIRA
# Margem de lucro
df['Lucro'] = df['Preço_Venda'] - df['Custo_Produto']
# ANÁLISE DE MARKETING
# ROI por canal
performance_marketing = df.groupby('Origem_Lead')['Preço_Venda'].sum()
# ANÁLISE OPERACIONAL
# Média de tempo de entrega
media_entrega = df['Tempo_Entrega'].mean()
# Exibir resultados
print("---Tabela com Cálculo de Lucro---")
print(df[['Categoria', 'Lucro', 'Status_Pagamento']])
print("\n --- Desempenho por canal de Marketing ---")
print(performance_marketing)
print(f'\n Tempo médio de Entrega: {media_entrega} dias')
