# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b) a = 2, b = 1


pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

a, b = pessoa #desempacota apeanas as chaves
print(a, b)

c, d = pessoa.values() #desempacota os valores das chaves
print(c, d)

e, f = pessoa.items() #desempacota uma tupla de chave e valor para cada variável
print(e, f)

for tupla in pessoa.items():
  print(tupla)

for chave, valor in pessoa.items():
  print(chave, valor)


#----------------------------------------------------------------------------------------------
pessoa2 = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}


dados_pessoa =  {
  'idade' : 16,
  'altura' : 1.70,
}

print('PESSOA COMPLETA -----------------------------')
pessoa_completa = {**pessoa, **dados_pessoa} #desempacota as as chaves e valores de um dicionário dentrod e outro
print(pessoa_completa)


#args e kwargs ------------------------------------------------------------------------------
#args = argumentos não nomeados
#kwargs = argumentos nomeados

def mostro_argumentos_nomeados(*args, **kwargs):
  print('Não nomeados: ', args)
  for chave, valor in kwargs.items():
    print(chave, valor)
  
# mostro_argumentos_nomeados(1, 2, nome='Joana', sobrenone='Rodrigues')
mostro_argumentos_nomeados(**pessoa2)