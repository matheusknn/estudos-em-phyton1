"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0

while contador <= 100:
  contador += 1

  if contador == 6:
    print('Não vou mostrar o 6')
    continue #volta para o while pulando o resto da operação, nesse caso o 6 não será printado

  if contador >= 10 and contador <=  27:
    continue
  
  print(contador)

  if contador == 40:
    break

print('Acabou')