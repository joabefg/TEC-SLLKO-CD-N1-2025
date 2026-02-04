import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importar os dados 
df = pd.read_csv('dados_estudantes.csv', sep=';', decimal='.',
encoding='utf-8-sig')
dados = df['Notas']

# 2. Cálculos das medidas
# 2.1 Média
# (Soma de todos os valores) / (Números de Valores)
media = np.mean(dados)

# 2.2 Mediana
# Valor central ou média dos valores centrais
mediana = np.median(dados)

# 2.3 Desvio
# Diferença entre cada valor e a média
desvios = dados - media 

# 2.4 Desvio Absoluto
# Diferença absoluta (módulo) entre cada valor e a média 
desvios_absolutos = np.abs(dados - media)

# 2.5 Variância
# Diferença media entre os valores ao quadrado e a média
variancia = np.var(dados, ddof=1)