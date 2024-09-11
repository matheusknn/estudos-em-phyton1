"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

#Definição da função
def soma(x, y, z):
  print(x,  y, z)


soma(1, 2, 3) #argumento não nomeado posicional
soma(1, 2, z=5) #argumento nomeado 
soma(1, y = 3, z=5) #todos os argumentos após o argumento nomeado irá precisar ser nomeado também