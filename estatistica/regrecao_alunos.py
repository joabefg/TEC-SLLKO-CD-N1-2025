from sklearn.linear_model import LinearRegression
LinearRegression
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

intercepto = model.intercept_
coef_regressao = model.coef_[0]

print(f'Intercepto: {intercepto}')
print(f'Coeficiente de Regressão: {coef_regressao}')

# 1. Pedir a nota do aluno
print("*** SIMULADOR DE NOTA PREVISTA ***")
entrada = input("Digite a quantidade de horas estudantes:")
horas_estudos = float(entrada)

# 2. Calcular a nota usando a equação de regressão
# y = A + Bx
nota_prevista = intercepto + (coef_regressao * horas_estudos)

# 3. Exibir o resultado formatado
print(f'Com {horas_estudos} horas de estudo, sua nota prevista é: {nota_prevista:2f}')