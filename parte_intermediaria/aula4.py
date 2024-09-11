"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
  # print(y) #erro pois y n está no escopo da função escopo
  def outra_funcao():
      global x #global diz para alterar o x que está no escopo global, ou seja o x = 1
      x = 11 
      y = 2
      print(x, y)
  outra_funcao()
  print(x)

print(x)
escopo()