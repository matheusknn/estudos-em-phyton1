"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
  if z is not None:
    print(f'{x=} {y=} {z=}')
  else:
    print(f'{x=} {y=}')

soma(1,3)
soma(1,3,6)
soma(z=10, x=32, y=31)