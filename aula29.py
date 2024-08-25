"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# try:
#   numero_inteiro_digitado = input('Digite um número inteiro: ')
#   numero_inteiro_convertido = int(numero_inteiro_digitado)
#   numero_e_par = numero_inteiro_convertido % 2 == 0
#   if numero_e_par:
#     print('Seu número é par')
#   else: 
#     print('Seu número é ímpar')
# except:
#   print('Seu número n é um inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_digitada = input('Qual é a hora de agr? ')

try:
  hora_digitada = float(hora_digitada)
  if hora_digitada >= 0 and hora_digitada <= 11:
    print('Bom dia')
  elif hora_digitada >= 12 and hora_digitada <= 17:
    print('Boa tarde')
  elif hora_digitada >= 18 and hora_digitada <= 23:
    print('Boa noite')
  else:
    print('Digite um horário válido')
except:
  print('pf digite um número')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# primeiro_nome_digitado = input('Digite seu primeiro nome ')
# quantidade_de_caracteres_do_nome = len(primeiro_nome_digitado)

# if quantidade_de_caracteres_do_nome <= 4:
#   print('Seu nome é curto')
# elif quantidade_de_caracteres_do_nome >= 5 and quantidade_de_caracteres_do_nome <= 6:
#   print('Seu nome é normal!')
# else:
#   print('Seu nome é muiiiito grande')
