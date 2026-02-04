import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados
df = pd.DataFrame({
    'alunos': ['Matheus', 'Fernando', 'Ana', 'Beatriz', 'Bruna'],
    'estudo_h': [2, 4, 6, 8, 10],
    'notas': [50, 70, 85, 95, 100],
    'videogame_h': [9, 8, 5, 4, 2]
})
# 2. Calcular a matriz de correlação
matriz_corr = df.corr(numeric_only=True)
print(matriz_corr)
# 3. Criar gráfico de dispersão
fig, (disp, calor) = plt.subplots(1, 2, figsize=(10,5))
sns.regplot(x = 'estudo_h', y = 'notas', data = df, truncate=False, ax=disp)
disp.set_title('Gráfico de Dispersão')
disp.grid(True)
# 3.1 Criar o heatmap
sns.heatmap(matriz_corr,
            annot=True,
            cmap="coolwarm",
            fmt=".2f",
            ax = calor)
calor.set_title("Mapa de Calor de Correlação")

# 4. Exibir Gráfico
plt.show()

