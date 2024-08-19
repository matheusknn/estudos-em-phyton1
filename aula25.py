"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome_do_usuario = input('Digite Seu Nome: ')
idade_do_usuario = input('Digite Sua Idade: ')
nome_invertido = nome_do_usuario[::-1]
letras_do_nome = len(nome_do_usuario)
primeita_letra_nome = nome_do_usuario[0]
ultima_letra_nome = nome_do_usuario[-1]

if nome_do_usuario and idade_do_usuario:
  print(f'seu nome é {nome_do_usuario}')
  print(f'Seu nome invertido é {nome_invertido}')

  if ' ' in nome_do_usuario: 
    print('seu nome contém espaços')
  else:
    print('seu nome n contém espaços')

  print(f'seu nome tem {letras_do_nome} letras')
  print(f'A primeira letra do seu nome é {primeita_letra_nome}')
  print(f'A última letra do seu nome é {ultima_letra_nome}')
else:
  print("Desculpe, você deixou campos vazios.") 