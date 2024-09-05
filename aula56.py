# Desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# a, b, c, *resto = lista
# m, h, *numeros, tres, e = lista
# print(m, h, tres, e)

print('Maria', 'Helena', 1, 2, 3, 'Eduarda') # =
print(*lista) #é como se tivesse passando todos os argumentos da lista de uma vez na função print
print(*string)
print(*salas)
print(*salas, sep='\n')