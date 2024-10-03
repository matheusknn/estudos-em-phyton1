#try, except, else e finally
# a = 18
# b = 0
# c = a / b

try:
  a = 18
  b = 0
  c = a / b
except ZeroDivisionError as e: #e vira instância da classe ZeroDivisionError
  print(e.__class__.__name__)
  print(e)
except NameError:
  print('alguma variável não está definida')
except (TypeError, IndexError)  as error:
  print('TypeError + IndexError')
  print('MSG: ', error.__class__.__name__)
except Exception:
  print('ocorreu algum erro')


print('continuar')