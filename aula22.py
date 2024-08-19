"""
Interpolação básica de strings = criar strings dinâmicas substituindo parte por expressões
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'matheus'
preco = 213231.123123
variavel = '%s, o preço é R$%f' % (nome, preco)
print(variavel)
print('o hexadecimal de %d é %04x' % (15,15))