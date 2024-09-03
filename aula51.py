import os
lista_de_compras = []

while True:
  print('Selecione uma opção: ')
  opcao_digitada = input('[i]nserir  [a]pagar  [l]istar: ').lower()

  if opcao_digitada == 'i':
    os.system('cls')
    valor = input('Valor: ')
    lista_de_compras.append(valor)

  elif opcao_digitada == 'a':
    indice_digitado = input('Digite o índice do produto que deseja apagar: ')
    try:
      indice_digitado_inteiro = int(indice_digitado)
      del lista_de_compras[indice_digitado_inteiro]
    except ValueError:
      print('digite um número inteiro!')
    except IndexError:
      print('o índice não existe na lista!')
    except Exception:
      print('Erro desconhecido')

  elif opcao_digitada == 'l':
    os.system('cls')

    if len(lista_de_compras) == 0:
      print('Não há nada para listar!')

    for i, valor in enumerate(lista_de_compras):
      print(i, valor)
  else:
    print('Você não digitou uma opção válida!')

