import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importar os dados
df = pd.read_csv('estatistica/dados_estudantes.csv', sep=';', decimal='.', encoding='utf-8-sig')

dados = df['Notas']

# 2. Calcular a média
# 2.1 Média
# (soma dos valores) / (número de valores)
media = np.mean(dados)

# 2.2 Mediana
# Valor central ou media dos valores centrais
mediana = np.median(dados)

# 2.3 Desvio
# Diferença entre cada valor e a média
desvios = dados - media

# 2.4 Desvio Absoluto 
# diferença absoluta (modulo) entre cada valor e a média
desvios_absolutos = np.abs(dados - media)

# 2.5 Variancia 
# Diferença media entre os valores ao quadrado e a média
variancia = np.var(dados, ddof=1)

# 2.6 Desvio Padrão
# Raiz quadrada da variancia
desvio_padrao = np.std(dados, ddof=1)

# 2.7 Desvio Médio Absoluto
mad = np.mean(desvios_absolutos)

# Exibir os dados
resultados_estatisticos = {
    'Metrica Estatística': [
        'media', 'mediana', 'Desvio Padrão', 'Variancia', 'Desvio Absoluto, Medio Absoluto'
    ],
    'valor Calculado': [
        media, mediana, desvio_padrao, variancia, mad
    ]
}
df_resultados = pd.DataFrame(resultados_estatisticos)
print(df_resultados.round(3))
