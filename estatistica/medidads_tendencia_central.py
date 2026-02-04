import pandas as pd
import numpy as np
from scipy.stats import trim_mean

df_dados_brutos = pd.read_csv('estatistica/taxa_homicidios.csv')

# media
media_populacao = df_dados_brutos['Populacao'].mean()
media_homicidios = df_dados_brutos['Taxa homicidios'].mean()
# mediana
mediana_populacao = df_dados_brutos['Populacao'].median()
mediana_homicidios = df_dados_brutos['Taxa homicidios'].median()
# media aparada
proporcao_corte = 0.1 # 10%
media_aparada_pop = trim_mean(df_dados_brutos['Populacao'], proportiontocut=proporcao_corte)
media_aparada_homi = trim_mean(df_dados_brutos['Taxa homicidios'], proportiontocut=proporcao_corte)
# media ponderada
media_ponderada = np.average(df_dados_brutos['Taxa homicidios'], weights=df_dados_brutos['Populacao'])
# Exibir dados
dataframe_medidas = pd.DataFrame({
    'Populacao': [media_populacao, media_aparada_pop, mediana_populacao, np.nan],
    'Taxa de homicidios': [media_homicidios, media_aparada_homi, mediana_homicidios, media_ponderada]
}, index=['Média','Média Aparada','Mediana','Média Ponderada'])
print(dataframe_medidas.to_string(float_format="%.2f"))
# Moda
frequencia_populacao = df_dados_brutos['Populacao'].value_counts()
frequencia_homicidios = df_dados_brutos['Taxa homicidios'].value_counts()
moda_populacao = frequencia_populacao[frequencia_populacao > 1]
moda_homicidios = frequencia_homicidios[frequencia_homicidios > 1]
if moda_homicidios.empty:
    print("Taxa de homicídios é amodal")
else:
    print(f"Moda Taxa de Homicídios: {moda_homicidios}")
    if len(moda_homicidios) > 2:
        print("Taxa de Homicídios é multimodal")
    if len(moda_homicidios) == 2:
        print("Taxa de Homicídios é bimodal")
    if len(moda_homicidios) == 1:
        print("Taxa de Homicídios é unimodal")
        print("Taxa de Homicídios é unimodal")