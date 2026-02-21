import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge, Lasso

#1. 
df = pd.read_csv("estatistica/house_sales.csv", delimiter="	")
x = df[['SqFtTotLiving', 'YrBuilt', 'Bathrooms']]
y = df['SalePrice']

# Dividir em treino e teste 80%, 20% teste
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#criar modelo e testar
modelo = LinearRegression()
modelo.fit(x_train, y_train)
#testar e prever o modelo
y_pred = modelo.predict(x_test)
#exibir os resultados
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_}")
print(f"R2 score: {r2_score(y_test, y_pred)}")
#Real vs Prevsito
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--r', linewidth=2)
plt.title('Real vs Previsto')
plt.xlabel('Preço Real')
plt.ylabel('Preço Previsto')
plt.show()