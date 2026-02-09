import pandas as pd
import numpy as np
from scipy.stats import trim_mean

df_dados_brutos=pd.read_csv('estatistica/Taxa_homicidios.csv')
#media
media_populacao = df_dados_brutos['Populacao'].mean()
media_homicidios = df_dados_brutos['Taxa Homicidios'].mean()

#mediana
mediana_populacao = df_dados_brutos['Populacao'].median()
mediana_homicidios = df_dados_brutos['Taxa Homicidios'].median()

#media aparada
proporcao_corte = 0.1 #10%
media_aparada_pop = trim_mean(df_dados_brutos['Populacao'],
proportiontocut=proporcao_corte)
media_aparada_homi = trim_mean(df_dados_brutos['Taxa Homicidios'], proportiontocut=proporcao_corte)
#media ponderada
meida_ponderada = np.average(df_dados_brutos['Taxa Homicidios'], weights=df_dados_brutos['Populacao'])
# Exibir Dados
dataframe_madidas = pd.DataFrame({
    'Populacao': [media_populacao, media_aparada_pop, mediana_populacao, np.nan],
    'Taxa de Homicidios': [media_homicidios, media_aparada_homi, mediana_homicidios, meida_ponderada]
}, index=['Média', 'Média_aparada', 'mediana', 'Média_ponderada'])
print(dataframe_madidas.to_string(float_format="%.2f"))
#Moda