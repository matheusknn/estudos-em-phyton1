"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] #deleta o índice 2 da lista e o python reorganiza a lista(tomar cuidado com processamento)
# print(lista)
lista.append(50) #adiciona ao final da lista
print(lista)
lista.pop()#remove o último valor da lista e retorna ele
print(lista)
ultimo_valor = lista.pop()
print(f'o último valor removido da lista foi: {ultimo_valor}')