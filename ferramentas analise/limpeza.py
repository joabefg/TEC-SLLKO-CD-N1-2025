import pandas as pd
import numpy as np

# importar csv
df = pd.read_csv('ferramentas analise/dados.csv')
print(df)

# 2. Remover duplicatas
df = df.drop_duplicates(subset=['ID_Pedido'], keep='first')
print(df)

# 3. Captular Produtos
df['Produto'] = df['Produto'].str.strip().str.capitalize()
print(df)

# 4. Substituir Incorretos
df['Produto'] = df ['Produto'].replace('Noteboke', 'Notebook')
print(df)