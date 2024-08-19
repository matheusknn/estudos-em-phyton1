"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

#exercício ----------------------------------
primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

if primeiro_valor > segundo_valor: 
  print(f'o primeiro valor ={primeiro_valor} é maior que o segundo valor ={segundo_valor}')
else:
    print(f'o segundo valor ={segundo_valor} é maior que o primeiro valor ={primeiro_valor}')