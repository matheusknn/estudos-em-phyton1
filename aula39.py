"""
For + Range
range -> range(start, stop, step)
"""

numeros = range(10) #pega números de 0 a 9
numeros = range(5,10) #pega os números de 5 a 9 (5,6,7,8,9)
numeros = range(5,10, 2) #pega os números de 5 a 9  e pula de 2 em 2 (5, 7, 9)
numeros = range(0, -10, -1) #pega os números de 0 a -9  e pula de -1 em -1 (0,-1,-2...)


for numero in numeros:
  print(numero)