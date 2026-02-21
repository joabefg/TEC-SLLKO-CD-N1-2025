import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Criando um dataset fictício
data = {
    'tamanho_m2': [50, 60, 80, 100, 120, 150, 30, 85, 110, 140],
    'quartos': [1, 2, 2, 3, 3, 4, 1, 2, 3, 4],
    'idade_anos': [5, 10, 2, 1, 15, 8, 20, 5, 3, 12],
    'preco': [250000, 320000, 450000, 580000, 610000, 750000, 150000, 430000, 590000, 700000]
}
'''
df = pd.DataFrame(data)
# 2. Separando Variáveis Independentes (X) e Dependente (y)
X = df[['tamanho_m2', 'quartos', 'idade_anos']]
y = df['preco']
'''
df = pd.read_csv('estatistica/house_sales.csv')
X = df[['SqFtTotLiving', 'Bedrooms', 'YrBuilt']]
y = df['SalePrice']

# 3. Dividindo em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Criando e treinando o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Fazendo previsões
y_pred = modelo.predict(X_test)

# 6. Exibindo Resultados
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"R² Score: {r2_score(y_test, y_pred):.2f}")

# Configurando o estilo
sns.set_theme(style="whitegrid")
plt.figure(figsize=(15, 5))

# --- Gráfico 1: Real vs Previsto ---
plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.title('Real vs. Previsto')
plt.xlabel('Preço Real')
plt.ylabel('Preço Previsto')

# --- Gráfico 2: Gráfico de Resíduos ---
residuos = y_test - y_pred
plt.subplot(1, 2, 2)
sns.scatterplot(x=y_pred, y=residuos)
plt.axhline(y=0, color='r', linestyle='--')
plt.title('Gráfico de Resíduos')
plt.xlabel('Previsão do Modelo')
plt.ylabel('Erro (Resíduo)')

plt.tight_layout()
plt.show()

# --- Gráfico 3: Importância das Variáveis ---
plt.figure(figsize=(8, 4))
coefs = pd.Series(modelo.coef_, index=X.columns)
coefs.plot(kind='barh', color='teal')
plt.title('Impacto de cada variável no Preço')
plt.xlabel('Peso do Coeficiente')
plt.show()