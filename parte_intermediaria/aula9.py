"""
Higher Order Functions
Funções de primeira classe
"""

def saudar(msg):
  return msg
  
def executa(funcao, mensagem):
  return funcao(mensagem)
  
v = executa(saudar, 'Bom dia!')
print(v)