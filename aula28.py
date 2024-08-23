"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
v2 = 'a'
print(id(v1)) #função id busca o endereço de memória
print(id(v2))

#///////////////////////////////////////////////////////////////////////

condicao = True
passou_no_if = None #indica que a variável n foi inicializada

if condicao:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)