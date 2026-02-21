import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Dados
x = np.array([[2], [4], [6], [8], [10]])
y = np.array([50, 70, 85, 95, 100])

# 2. Treinando o modelo
modelo = LinearRegression()
modelo.fit(x, y)

# 3. Fazendo as previsões
y_pred = modelo.predict(x)

# 4. Calculando Métricas de Validação
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f"RMSE: A média de erro da nota é: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# 5. Cálculo dos resíduos
residuos = y - y_pred

# Gráfico 1: Gráfico de Resíduos
plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
plt.axhline(y=0, color='r', linestyle='--')
sns.scatterplot(x=y_pred, y=residuos)
plt.title("Gráfico de resíduos")
plt.xlabel("Valores previstos")
plt.ylabel("Resíduos")

# Gráfico 2: Histograma de resíduos
plt.subplot(1, 2, 2)
sns.histplot(residuos, color='purple')
plt.title('Distribuição dos Resíduos')
plt.xlabel('Tamanho do Erro')
plt.ylabel('Frequência')

plt.show()