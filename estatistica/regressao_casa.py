import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
 
data = {
    'tamanho_m2': [50, 60, 80, 100, 120, 150, 30, 85, 110, 140],
    'quartos': [1, 2, 2, 3, 3, 4, 1, 2, 3, 4],
    'idade_anos': [5, 10, 2, 1, 15, 8, 20, 5, 3, 12],
    'preco': [250000, 320000, 450000, 580000, 610000, 750000, 150000, 430000, 590000, 700000]
}
# Separando variaveis independentes das dependentes
df = pd.DataFrame(data)
x = df[['tamanho_m2', 'quartos', 'idade_anos']]
y = df['preco']

# Dividir em treino e teste(80% treino, 20% teste)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Criar modelo e treinar
modelo = LinearRegression()
modelo.fit(x_train, y_train)

# Fazer previsão
y_pred = modelo.predict(x_test)

# Exibir resultados
print(f"Coeficientes de regressão: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_:.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

plt.figure(figsize=(8, 4))
coefs = pd.Series(modelo.coef_, index=x.columns)
coefs.plot(kind='barh', color='teal')
plt.title('Impacto de cada variável no Preço')
plt.xlabel('Peso do coeficiente')
plt.show()