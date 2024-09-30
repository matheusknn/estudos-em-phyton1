# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

print(produto.items())

dc = {
  chave: valor.upper()
  if isinstance(valor, str) else valor
  for chave, valor 
  in produto.items()
  if chave == 'categoria' #filtro só inclui se a chave tiver o valor 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
print(dict(lista))

s1 = {i for i in range(10)}
print(s1)
print(set(range(10)))