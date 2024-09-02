"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append(21) #adiciona ao final da lista
print(lista)
ultimo_item_lista = lista.pop() #remove o último item da lista e retorna ele
print(lista, f'o item removido foi {ultimo_item_lista}')
del lista[-1] #deleta algo da lista
print(lista)
# lista.clear() #limpa os itens da lista
lista.insert(0, 41) #adiciona um item no index passado de primeiro argumento e reorganiza os outros itens da lista para frente
print(lista)