primeiro_valor = int(input('insira o primeiro valor: '))
segundo_valor = int(input('insira o segundo valor: '))

if primeiro_valor > segundo_valor:
  print(f'o primeiro valor {primeiro_valor} é  maior q o segundo valor {segundo_valor}')
elif segundo_valor > primeiro_valor:
  print(f'o segundo valor {segundo_valor} é  maior q o primeiro valor {primeiro_valor}')
else:
  print('nenhum valor é maior q o outro')