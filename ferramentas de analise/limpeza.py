import pandas as pd
import numpy as np

# 1. Importar o arquivo csv
df = pd.read_csv('ferramentas de analise/dados.csv')
print(df)

# 2. Remover duplicatas
df = df.drop_duplicates(subset=['ID_Pedido'], keep='first')
print(df)

# 3. Captular produtos
df['Produto'] = df['Produto'].str.strip().str.capitalize()
print(df)

# 4. Substituir incorretos
df['Produto'] = df['Produto'].replace('Noteboke','Notebook')
print(df)
