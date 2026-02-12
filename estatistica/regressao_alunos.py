from sklearn.linear_model import LinearRegression
import pandas as pd


df = pd.DataFrame({
    'alunos': ['Matheus', 'Fernando', 'Ana', 'Beatriz', 'Bruna'],
    'estudo_h': [2, 4, 6, 8, 10],
    'notas': [50, 70, 85, 95, 100],
    'videogame_h': [9, 8, 5, 4, 2]
})

predictors = ['estudo_h']
outcome = 'notas'

model = LinearRegression()
model.fit(df[predictors], df[outcome])

intercept = model.intercept_
coef_regressao = model.coef_[0]

print(f'Intercepto: {intercept}')
print(f'Coeficiente de regressão: {coef_regressao}')

#1. pedir a nota do aluno
print("--- simulador de nota prevista ---")
entrada = input ("Digite o número de horas estudadas: ")
horas_estudadas = float(entrada)

#2. calcular a nota usando a equação de regressão
#y = A + Bx
nota_prevista = intercept + (coef_regressao * horas_estudadas)

#3. exibir o resultado
print(f'Com {horas_estudadas} horas de estudo, a nota prevista é: {nota_prevista:.2f}')