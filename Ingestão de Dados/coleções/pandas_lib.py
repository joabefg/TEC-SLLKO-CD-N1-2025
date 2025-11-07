"""
Fundamentos e como usar a biblioteca Pandas
"""
import pandas as pd

class PandasLib:
    def criar_series_padrao(self):
        notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])
        print(f"Series simples: \n{notas}")
        return notas
    
    def criar_series_com_indice(self):
        lst_matriculas = ['M02', 'M05', 'M13', 'M14', 'M19']
        lst_nomes = ['Bob', 'Dayse', 'Bill', 'Cris', 'Jimi']
        alunos = pd.Series(lst_nomes, index=lst_matriculas)
        print(f"Series com índice matrículas: \n{alunos}")
        # atribuir nomes às colunas
        alunos.name = "alunos"
        alunos.index.name = "mat"
        print(f"Series com índice nomeado: \n{alunos}")

if __name__ == "__main__":
    inst = PandasLib()
    series_notas = inst.criar_series_padrao()
    inst.criar_series_com_indice()