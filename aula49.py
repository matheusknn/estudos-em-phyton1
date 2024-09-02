"""
Introdução ao empacotamento e desempacotamento
"""

nomes = ['Matheus', 'Kenji', 'Nishimura']
# nome1, nome2, nome3 = nomes
# print(nome2) #nome2 recebe kenji

_, nome2, *_ = nomes #_ indica que a variável n será utilizada
print(nome2, _) #* retorna os valores que não foram inclusos em nenhuma variável