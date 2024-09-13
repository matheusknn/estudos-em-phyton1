"""
args - Argumentos não nomeados
* - *args(empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma(x, y):
#   return x + y

def soma(*args): 
  soma = 0
  # args = list(args)
  print(args)#tupla(lista não alterável) com todos os argumentos colocados na função
  for numero in args:
    soma += numero
  print(f'o resultado da sua soma é {soma}')
  return soma

numeros = 1,2,3,4,5,9 #tupla

soma1 = soma(*numeros) #desempacotando
print(soma1)

print(sum((1, 2, 3, 4, 5, 6)))