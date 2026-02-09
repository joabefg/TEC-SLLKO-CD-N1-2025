import pandas as pd
import matplotlib.pyplot as plt

resultados = []
def calcular_medidas_var(df, col):
    media = df[col].mean()
    amp = df[col].max() - df[col].min()
    var = df[col].var()
    std = df[col].std()
    cv = (std / media) * 100
    return {
        'Gra': col,
        'Amp': amp,
        'Var': var,
        'Std': std,
        'CV': cv
    }
# 1. Biometria em Recrutas
dados_biometricos = {
    'peso_kg': [70, 85, 78, 92, 65, 88, 74],
    'altura_m': [1.75, 1.80, 1.72, 1.85, 1.68, 1.78, 1.74]
}
df_bio = pd.DataFrame(dados_biometricos)
res_peso = calcular_medidas_var(df_bio, 'peso_kg')
res_alt = calcular_medidas_var(df_bio, 'altura_m')
resultados.append(res_peso)
resultados.append(res_alt)
df_estatisticos = pd.DataFrame(resultados)
print(df_estatisticos)
# gráfico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(['Peso (CV%)', 'Altura (CV%)'], [res_peso['CV'], res_alt['CV']])
ax1.set_title('Comparação da Variabilidade')

#2. Controle de Sódio
dados_alimento = {
    'sodio_mg':[150, 155, 148, 200, 152, 149, 151],
    'gordura_g':[10.2, 10.5, 9.8, 10.1, 10.3, 10.0, 9.9]
}
df_food = pd.DataFrame(dados_alimento)
res_sodio = calcular_medidas_var(df_food, 'sodio_mg')
resultados.append(res_sodio)
res_gord = calcular_medidas_var(df_food, 'gordura_g')
resultados.append(res_gord)
df_alimento = pd.DataFrame(resultados)
print(df_alimento)
ax2.bar(['sódio', 'Gordura'], [res_sodio['CV'], res_gord['CV']])
ax2.set_title('Instabilidade do Processo (CV%)')
plt.show()

#Batimentos cardiacos
dados_batimentos = {
    'Atleta':[50, 52, 48, 51, 49, 50, 51],
    'Sedentario': [80, 85, 78, 92, 88, 81, 84]
}
df_batimentos = pd.DataFrame(dados_batimentos)
res_atleta = calcular_medidas_var(df_batimentos, 'Atleta')
res_sedent = calcular_medidas_var(df_batimentos, 'Sedentario')
fig2, (axbx, axbr) = plt.subplots(1, 2, figsize=(12,5))
df_batimentos[['Atleta', 'Sedentario']].boxplot(ax=axbx)
axbx.set_title('Frequencia Cardiaca (BPM)')
axbr.bar(['Alteta', 'Sedentario'], [res_atleta['CV'], res_sedent['CV']])
axbr.set_title('Coeficiente de Variação (%) - Saúde')
plt.show()