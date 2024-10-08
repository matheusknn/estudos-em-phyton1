# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def checa_se_e_zero(b):
  if b == 0:
    raise ZeroDivisionError('Você está tentando dividir por zero')
  return True

def deve_ser_int_ou_float(n):
  if not isinstance(n, (int, float)):
    raise TypeError('a, deve ser int ou float')

def divide(a, b):
  deve_ser_int_ou_float(a)
  deve_ser_int_ou_float(b)
  checa_se_e_zero(b)
  return a / b


print(divide(8, 2))