import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SP500_DATA_CSV = 'estatistica/sp500_data.csv.gz'
SP500_SECTORS_CSV = 'estatistica/sp500_sectors.csv'

print('classificação setorial')
sp500_sym = pd.read_csv(SP500_SECTORS_CSV)
print(sp500_sym.head())

print('retorno diário')
sp500_px = pd.read_csv(SP500_DATA_CSV, index_col = 0)
print(sp500_px.head())

telecomSymbols = sp500_sym[sp500_sym['sector'] == 'telecommunications_services']['symbol']
print(telecomSymbols.head())

telecom = sp500_px.loc[sp500_px.index >= '2012-07-01', telecomSymbols]
print(telecom.head())

dados_correlacionados = telecom.corr()
print(dados_correlacionados.head())

etfs = sp500_px.loc[sp500_px.index > '2012-07-01', 
                    sp500_sym[sp500_sym['sector'] == 'etf']['symbol']]
print(etfs.head())

etfs_correlacionados = etfs.corr()
print(etfs_correlacionados.head())

fig, (telecomax, etfax) = plt.subplots(1, 2, figsize=(10,5))
telecomax = sns.heatmap(telecom.corr(), vmin=-1, vmax=1, cmap=sns.
diverging_palette(20, 220, as_cmap=True), ax=telecomax)
etfax = sns.heatmap(etfs_correlacionados, vmin=-1, vmax=1, cmap=sns.
diverging_palette(20, 220, as_cmap=True), ax=etfax)
plt.show()