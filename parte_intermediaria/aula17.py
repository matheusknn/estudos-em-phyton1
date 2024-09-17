# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
  print('Pergunta', pergunta['Pergunta'])
  print()

  for i, opcao in enumerate(pergunta['Opções']):
    print(f'{i}) {opcao}')
  print()  

  resposta_digitada = input('Digite o valor da resposta: ')

  acertou = False
  resposta_digitada_inteira = None

  if resposta_digitada.isdigit():
    resposta_digitada = int(resposta_digitada)

  if resposta_digitada_inteira is not None:
    print()

