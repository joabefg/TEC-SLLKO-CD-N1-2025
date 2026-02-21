import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Dados: Horas de Estudo vs Nota (Dados do seu slide)
X = np.array([[2], [4], [6], [8], [10]])
y = np.array([50, 70, 85, 95, 100])

# 1. Dados: Tamanho (m2) vs Preço (Milhares de R$)
X = np.array([[100], [150], [200], [250], [300]]) # Área
y = np.array([250, 380, 490, 620, 750])           # Preço Real

# 2. Treinando o modelo (Onde o RSS é minimizado)
modelo = LinearRegression()
modelo.fit(X, y)

# 3. Fazendo previsões (Valores Ajustados / y-chapéu)
y_pred = modelo.predict(X)

# 4. Calculando as Métricas de Validação
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f"RMSE: R$ {rmse:.2f} mil")
print(f"R² Score: {r2:.4f}")


# 3. Cálculo dos Resíduos
residuos = y - y_pred
# --- BLOCO DE GRÁFICOS DE VALIDAÇÃO ---
plt.figure(figsize=(12, 5))

# Gráfico 1: Gráfico de Resíduos (Residual Plot)
plt.subplot(1, 2, 1)
plt.axhline(y=0, color='r', linestyle='--') # Linha no zero
sns.scatterplot(x=y_pred, y=residuos)
plt.title('Gráfico de Resíduos\n(O erro é aleatório?)')
plt.xlabel('Valores Previstos (ŷ)')
plt.ylabel('Resíduo (e)')

# Gráfico 2: Histograma de Resíduos
plt.subplot(1, 2, 2)
sns.histplot(residuos, kde=True, color='purple')
plt.title('Distribuição dos Resíduos\n(O erro segue uma Normal?)')
plt.xlabel('Tamanho do Erro')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()

# Métricas no console
print(f"RMSE: {np.sqrt(mean_squared_error(y, y_pred)):.2f}")
print(f"R2 Score: {r2_score(y, y_pred):.4f}")

# ********************************************************************************

# Definindo o tamanho da casa que queremos prever
tamanho_novo = np.array([[180]])

# Fazendo a previsão
preco_previsto = modelo.predict(tamanho_novo)

print(f"Para uma casa de 180 m², o preço estimado é: R$ {preco_previsto[0]:.2f} mil")