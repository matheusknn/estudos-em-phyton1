"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Matheus', 'Kenji', 'Nishimura']
lista.append('Romário')
print(lista)

lista_enumerada = enumerate(lista) 

for item in lista_enumerada:
  indice, nome = item 
  print(f'índice: {item[0]}, item: {item[1]}')