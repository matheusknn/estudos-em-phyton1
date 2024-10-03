
try:
  print('Abrir Arquivo')
  #open
  8/0
except ZeroDivisionError as error:
  print('Dividiu por 0')
else: #é executado caso o bloco dentro do try não dê nenhum erro
  print('Não deu erro')
finally: #bloco que sempre será executado mesmo q ocorra um erro
  print('Fechar arquivo')