"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)

lista = list() #criando uma lista usando a função
#                   0     1      2      3     4
lista_colchetes = [123, True, 'Kenji', 20.2, []] #lista vazia comparado "booleanmente" é vazia
print(lista_colchetes)
lista_colchetes[2] = 'Matheus'
print(lista_colchetes)