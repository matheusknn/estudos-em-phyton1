# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
  print(item, isinstance(item, str))
  if isinstance(item, (int, float)): #verifica se item é int OU float
    print(item, item * 2)