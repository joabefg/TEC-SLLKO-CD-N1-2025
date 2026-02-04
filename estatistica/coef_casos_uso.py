import pandas as pd
import matplotlib.pyplot as plt

resultados = []
def calcular_medidas_var(df, col):
    media = df[col].mean()
    amp = df[col].max() - df[col].min()
    var = df[col].var()
    std = df[col].std()
    cv = (std / media) * 100
    return{
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

# Gráfico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.bar(['Peso (CV%)', 'Altura (CV%)'], [res_peso['CV'], res_alt['CV']])
ax1.set_title('Comparação da Variabilidade')
plt.show()