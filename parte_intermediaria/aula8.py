# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
  resultado = 1

  for numero in args:
    resultado *= numero #= 1*2*3*4*5

  return resultado

multiplicacao = multiplica(1, 2, 3, 4, 5)
print(multiplicacao)
print(1*2*3*4*5)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def classificar(numero):
  if numero % 2 == 0:
    print('o número é par')
  else:
    print('o número é ímpar')

    