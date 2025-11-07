"""
Exemplos de uso das diferente coleções
"""
class Colecoes:
    def listas(self):
        # lista flexível
        lista_flexivel = [123, 3.14, "texto", True]
        # ordenada
        posicao_dois = lista_flexivel[1]
        ultima_posicao = lista_flexivel[-1]
        print(lista_flexivel[-1] == lista_flexivel[2])
        print(f"segunda posição: {posicao_dois} - último item: {ultima_posicao}")
        # mutável
        print(f"lista inteira: {lista_flexivel}")
        lista_flexivel.remove(3.14)
        lista_flexivel.append("novo item")
        print(f"lista após remoção: {lista_flexivel}")
        # lista aninhada (nested)
        matriz = [[2, 4, 6],
                  ["dois", "quatro", "seis"],
                  [2.4, 4.6, 6.2]]
        print(f"matriz: \n{matriz}")

    def tuplas(self):
        tupla_numeros = (1, 2, 4, 6, 6, 12, 18)
        nova_tupla = tupla_numeros * 2
        print(f"tupla numeros: {tupla_numeros} - nova tupla: {nova_tupla}")

    def conjuntos(self):
        conjunto_numeros = {1, 1, 2, 2, 3, 3, 4, 4}
        print(f"conjunto de números: {conjunto_numeros}")
        # funções de conjuntos
        conjunto_a = {'cadeira', 'mesa', 'computador', 'quadro'}
        conjunto_b = {'apagador', 'computador'}
        uniao = conjunto_a.union(conjunto_b)
        interseccao = conjunto_a.intersection(conjunto_b)
        diferenca = conjunto_a.difference(conjunto_b)
        print(f'união: {uniao} \n intersecção: {interseccao} \n diferença: {diferenca}')

    def dicionarios(self):
        # todo dicionário possui um conjunto de chave e valor
        dict = {'chave': 'valor', 'atributo': 'valor', 'coluna': 'valor'}
        print(f" valor na chave atributo: {dict['atributo']}")
        # Acessar chave e valor funcionarios
        funcionario = {'nome': 'Maria', 'cargo': 'psicóloga', 'setor': 'RH'}
        print(f" funcionário \n dados: {funcionario}")
        print(f" o nome do funcionário é {funcionario['nome']}")
        # dicionários podem ser alterados
        funcionario['cargo'] = 'Recrutadora'
        funcionario['idade'] = 25
        print(f"dados após alteração: {funcionario}")
        candidato = {'nome': {'primeiro': 'Maria', 'sobrenome': 'Silva'},
                    'funções': ['dev', 'tester', 'devops'],
                    'idade': 25}
        print(f"dados do candidato: {candidato}")
        print(f"sobrenome do candidato: {candidato['nome']['sobrenome']}")

if __name__ == "__main__":
    instancia = Colecoes()
    instancia.listas()
    print("-"*30)
    instancia.tuplas()
    print("-"*30)
    instancia.conjuntos()
    print("-"*30)
    instancia.dicionarios()