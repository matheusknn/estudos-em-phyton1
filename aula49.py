"""
Introdução ao empacotamento e desempacotamento
Tipo tupla - lista imutável
"""

nomes = ['Matheus', 'Kenji', 'Nishimura']
# nome1, nome2, nome3 = nomes
# print(nome2) #nome2 recebe kenji

_, nome2, *_ = nomes #_ indica que a variável n será utilizada
print(nome2, _) #* retorna os valores que não foram inclusos em nenhuma variável]


#--------------------------Tupla(lista imutável)---------------------------------------------------
personagens = 'Jiraya', 'Naraito', 'Kushina'
nomes_tupla = tuple(nomes)
# personagens[1] = 'Teta' #gera erro, pois uma tupla é um tipo de dado imutável