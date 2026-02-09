import numpy as np
import matplotlib.pyplot as plt

# Tempo de entrega pizza em minutos
dominos = [28, 30, 31, 29, 30, 32, 29, 30, 31, 30]
italiana = [15, 45, 20, 55, 10, 60, 25, 50, 30, 40]
# Cálculos dominos
dm_media = np.mean(dominos)
dm_amplitude = np.max(dominos) - np.min(dominos)
dm_dam = np.mean(np.abs(dominos - dm_media))
dm_variancia = np.var(dominos, ddof=1)
dm_desvio_padrao = np.std(dominos, ddof=1)
dm_cv = (dm_desvio_padrao / dm_media) * 100
# Cálculos italiana
it_media = np.mean(italiana)
it_amplitude = np.max(italiana) - np.min(italiana)
it_dam = np.mean(np.abs(italiana - it_media))
it_variancia = np.var(italiana, ddof=1)
it_desvio_padrao = np.std(italiana, ddof=1)
it_cv = (it_desvio_padrao / it_media) * 100
# Exibir dados> < esquerda - > direita - ^ centralizado
print(f"{'Métrica':<20} | {'Dominos':<20} | {'Italiana':<20}")
print(f"{'Média':<20} | {dm_media:<20} | {it_media:<20}")
print(f"{'Amplitude':<20} | {dm_amplitude:<20} | {it_amplitude:<20}")
print(f"{'DAM':<20} | {dm_dam:<20} | {it_dam:<20}")
print(f"{'Variância':<20} | {dm_variancia:<20.2f} | {it_variancia:<20.2f}")
print(f"{'Desvio Padrão':<20} | {dm_desvio_padrao:<20} | {it_desvio_padrao:<20}")
print(f"{'Coef. Variação':<20} | {dm_cv:<20} | {it_cv:<20}")

# Gráfico
restaurantes = ['Dominos', 'Italiana']
cv_valores = [dm_cv, it_cv]
plt.figure(figsize=(8, 6))
plt.bar(restaurantes, cv_valores, color=['#4CAF50','#F44336'])
plt.ylabel('Coeficiente de Variação (%)', fontsize=12)
plt.title('Comparação de Instabilidade (CV%) entre Restaurantes', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()