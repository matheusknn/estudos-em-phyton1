import sys
#Generator expression, Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__'] #iterável guarda os valores sequencialmente
iterator = iterable.__iter__() #iterator sabe entregar o próximo valor do iterável

lista = [n for n in range(1000)]
generator = (n for n in range(1000)) #generator
print(sys.getsizeof(lista)) #retorna o tamanho da lista em bytes na memória
print(sys.getsizeof(generator)) #generator n salva todos os valores na memória ele entrega apenas 1 valor por vez

print(next(generator))

for n in generator:
  print(n)
