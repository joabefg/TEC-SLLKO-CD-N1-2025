from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.DataFrame({
    'alunos': ['Mateus', 'Fernando', 'Ana', 'Beatriz', 'Bruna'],
    'estudo_h': [2, 4, 6, 8, 10],
    'notas': [50, 70, 85, 95, 100]
})

predictors = ['estudo_h']
outcome = 'notas'

model = LinearRegression()
model.fit(df[predictors], df[outcome])

intercepto = model.intercept_
coef_regressao = model.coef_[0]
print(f'intercepto: {intercepto}')
print(f'Coeficiente de Regressão: {coef_regressao}')

# Pedir nota do aluno
print('*** SIMULADOR DE NOTA PREVISTA ***')
entrada = input("Digite a quantidade de horas estudadas: ")
horas_de_estudo = float(entrada)

#2. Calcular nota usando equação de regressão
#y = A + Bx
nota_prevista = intercepto + (coef_regressao * horas_de_estudo)

#3. exibir horas de estudo
print(f'com {horas_de_estudo} horas de estudo, sua nota prevista é {nota_prevista:.2f}')
