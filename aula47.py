"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

nome = 'Kenji'
outra_variavel = nome
# nome[1] = 'C' #causa erro pois string é um dado imutável, porém, ainda podemos atribuir outro valor a variável
nome = 'Matheus'
print(nome)
print(outra_variavel) 

nomes_a = ['Matheus', 'Kenji']
nomes_b = nomes_a #nomes_b aponta para o mesmo valor em memória que nomes_a(OBS: dados imutáveis como strings são copiados e não referênciados)

nomes_c = nomes_a.copy() #retorna diretamente os valores e não a referência
print(nomes_c)