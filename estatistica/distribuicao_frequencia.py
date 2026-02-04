import pandas as pd
import numpy as np
import matplotlib.pylab as plt

# 1. Gerar os Dados Brutos
notas = np.random.randint(5, 100, size=30)
# 2. Rol e n 
n = len(notas)
rol = np.sort(notas)
print(f"1. Rol: \n{rol} \n")
print(f"2. n: \n {n} \n")
# 3. Amplitude Total
AT = rol.max() - rol.min()
print(f"3. Amplitude total (AT): {AT} \n")
# 4. Amplitude das Classes
k_sturges = 1 + 3.322 * np.log10(n)
k = round(k_sturges)
print(f"4. Número de classes (k): {k} \n")
# 5. Amplitude das Classes
h_calc = AT / k
h = np.ceil(h_calc)
# 6. Limites das classes: Bins
bins = np.arange(rol.min(), rol.max() + h + 1, h )
bins_plot = np.arange(rol.min(), rol.max() + h, h)
# 7. Tabela de Frequência
frequencias_abs = pd.cut(rol, bins=bins, include_lowest=True, right= False).value_counts().sort_index()
print(f"Frequencia absolutas: \n {frequencias_abs} \n")
# 8. Gráfico - Histograma
plt.figure(figsize=(10, 6))
plt.hist(rol, bins=bins_plot, density=False)
plt.title('Histograma da Distribuição de Frequência')
plt.xlabel('Intervalos( Classes)')
plt.ylabel('Frequência Absoluta')
plt.xticks(bins_plot)
plt.grid(axis= 'y', alpha=0.5)
plt.show()