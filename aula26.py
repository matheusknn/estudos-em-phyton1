"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('vou dobrar o número que você digitar: ')

try:
  print('STR:', numero_str)
  numero_float = float(numero_str)
  print('FLOAT: ', numero_float)
  print(f'o dobro de {numero_float} é {numero_float * 2}')
except:
  print(f'{numero_str} não é um número, por favor digite algo válido!')

# if numero_str.isdigit(): 
#   print(f'o dobro de {numero_str} é {int(numero_str) * 2}')
# else:
#   print(f'{numero_str} não é um número, por favor digite algo válido!')  