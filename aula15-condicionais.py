entrada = input('você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
  print('você entrou no sistema')
  print('dentro do if')
elif entrada == 'sair':
  print('você saiu do sistema')
else:
  print('você n digitou algo válido')

print('fora dos blocos')