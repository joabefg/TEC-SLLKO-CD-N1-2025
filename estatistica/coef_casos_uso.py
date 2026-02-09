import pandas as pd
import matplotlib.pyplot as plt

resultados = []
def calcular_medidas_var(df, col,):
    media = df[col].mean()
    amp = df[col].max() - df[col].min()
    var = df[col].var()
    std = df[col].std()
    vc = (std / media) * 100
    return {
        'Gra': col,
        'Amp': amp,
        'Var': var,
        'Std': std,
        'VC': vc      
    }
# 1. Biometria em Recrutas peso_kg
dados_biometricos = {
    'peso_kg': [70, 75, 80, 85, 90, 95, 100],
    'altura_m': [1.70, 1.72, 1.74, 1.76, 1.78, 1.80, 1.82,]
}
df_bio = pd.DataFrame(dados_biometricos)
res_peso = calcular_medidas_var(df_bio, 'peso_kg')
res_alt = calcular_medidas_var(df_bio, 'altura_m')
resultados.append(res_peso) 
resultados.append(res_alt)  
df_estatisticas = pd.DataFrame(resultados)
print(df_estatisticas)
# grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))   
ax1.bar(['Peso(CV%)','Altura(CV%)'], [res_peso['VC'], res_alt['VC']])
ax1.set_title('Comparacão da Variabilidade') 
plt.show()

