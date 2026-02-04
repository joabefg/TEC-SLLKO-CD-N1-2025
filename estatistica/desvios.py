import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#1. carregar dados
df = pd.read_csv('estatistica/dados_estudantes.csv', sep=';', decimal='.', encoding='utf-8-sig')
dados = df['Notas']

#2. calculo das medidas
#2.1 media
#soma de todos os valores / numero de valores
media = np.mean(dados)

#2.2 mediana
#valor central ou a media dos valores centrais
mediana = np.median(dados)

#2.3 desvio
#diferente de cada valor e a media
desvios = dados - media

#2.4 desvio absoluto
# diferença abslota entre cada valor e a media
desvios_absolutos = np.abs(dados - media)

#2.5 variança
# diferença media entre os valores e a media
variancia = np.var(dados, ddof=1) 

#2.6 desvio padrão
#raiz quadrada da variancia
desvio_padrao = np.std(dados, ddof=1)

#2.7 coeficiente de variação
mad = np.mean(desvios_absolutos)

#exibir dados

resultados_estatisticas = {
    'Métrica Estatística': ['Média', 'Mediana', 'Variância', 'Desvio Padrão', 'Desvio Abs. medio'
    ],
    'Valor Calculado': [
        media, mediana, variancia, desvio_padrao, mad
    ]
}
df_resultados = pd.DataFrame(resultados_estatisticas)
print(df_resultados.round(3))