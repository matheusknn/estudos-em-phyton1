"""calculadora com while"""

while True:
  numero_1 = input('Digite um número: ')
  numero_2 = input('Digite outro número: ')
  operador = input('Digite um operador(+-/*): ')

  numeros_validos = None
  try:
    numero_1_float = float(numero_1)
    numero_2_float = float(numero_2)
    numeros_validos = True
  except:
    numeros_validos = None
    if numeros_validos is None:
      print('Você não digitou um número, por favor dígite um número')
      continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
      print('Operador inválido')
      continue

    if len(operador) > 1:
      print('Digite apenas 1 operador')
      continue
    
  sair = input('Deseja Sair? [s]im: ').lower().startswith('s')

  if sair is True:
    break
