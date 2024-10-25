# if / elif      / else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
  print('Você entrou no sistema')

  print(12345678)
elif entrada == 'sair':
  print('Você saiu do sistema')
else:
  print('Você digitou uma opção inválida')

print('fora dos blocos condicionais')