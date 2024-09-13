# Manipulando chaves e valores em dicionários

pessoa = {
  
}
lista = []
##
##

pessoa['nome'] = 'Matheus Kenji' #criando e atribuindo uma propriedade ao dict(dicionário)
print(pessoa['nome']) #acessando uma propriedade do dict(dicionário)

chave = 'idade'
pessoa[chave] = 21
print(pessoa[chave])

del pessoa[chave] #apagando a chave e o valor dessa chave
print(pessoa)


if pessoa.get('nome', None): #verifica se a chave existe no dicionário, caso não existe por padrão retorna None
  print('A chave existe')
else:
  print('A chave não existe')