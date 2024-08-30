"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# # for letra in texto
# texto = iter('Kenji') #__iter__(), função que entrega o objeto iterador que sabe iterar a string
# print(texto.__next__()) #K
# print(texto.__next__()) #e

texto = 'Matheus' #iterável: objetos capazes de retornar seus membros um de cada vez
# iterator = iter(texto)
# print(iterator)

# while True:
#   try:
#     letra = next(iterator)
#     print(letra)
#   except StopIteration:
#     break

for letra in texto:
  print(letra)