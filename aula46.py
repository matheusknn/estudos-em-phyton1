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
lista_a = [1,2,3,4,5,6]
lista_b = [7,8,9,10,11,12]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) #não retorna nada, porém, MUDA A PRÓPRIA LISTA
print(lista_c)