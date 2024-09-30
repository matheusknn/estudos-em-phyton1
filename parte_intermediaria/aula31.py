# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

def generator(n=0):
  yield 1 #vê o yield retorna o valor e pausa a função até o next ser chamado
  print('continuando...')
  yield 2 #pausa

gen = generator(n=0)
print(next(gen))
print(next(gen))

for i in gen:
  print(i)

#-----------------------------------------------------------------------------------
def generator2(n=0, maximum=10):
  while True:
    yield n
    n += 1

    if n > maximum:
      return
    
gen2 = generator2(maximum=1000)
for n in gen2:
  print(n)