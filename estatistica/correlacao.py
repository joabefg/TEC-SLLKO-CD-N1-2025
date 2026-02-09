import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#1. Carregar os dados
df = pd.DataFrame({
    'alunos': ['Mateus', 'Fernando', 'Ana', 'Beatriz', 'Bruna'],
    'estudo_h': [2, 4, 6, 8, 10],
    'notas': [50, 70, 85, 95, 100]
})
#2. Calcular a Matriz correlação
matriz_corr = df.corr(numeric_only=True)
print(matriz_corr)
#3. Criar grafico de disperção
fig, (disp, calor) = plt.subplots(1, 2, figsize=(10,5))
sns.regplot(x = 'estudo_h', y = 'notas', data = df, truncate=False, ax=disp)
disp.set_title('Grafico de Disperção')
#4 exibir grafico
plt.show()