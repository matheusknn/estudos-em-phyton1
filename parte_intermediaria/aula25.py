lista = []
for x in range(3): 
  for y in range(3):
    lista.append((x, y))

lista = [
  (x, y)
  for x in range(3)
  for y in range(3) #é como se fosse um for dentro de outro for
]

print(lista)