"""
Closure e funções que retornam outras funções
"""

def saudar_alguem(saudacao, nome):
  def saudar():
    return f'{saudacao} {nome}'
  return saudar

s1 = saudar_alguem('Bom dia!', 'Kenji')
s2 = saudar_alguem('Boa noite!', 'Kenji')
print(s1()) #Closure
print(s2)
