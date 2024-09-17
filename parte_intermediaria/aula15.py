# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy) 
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

d1 = {
  'c1' : 1,
  'c2' : 2
}

d2 = d1 #aponta para o mesmo dicionário

d3 = d1.copy() #copy faz uma CÓPIA RASA, OU SEJA, SÓ COPIA OS DADOS IMUTÁVEIS para uma nova variável, PORÉM, os dados mutáveis como tuplas e dicts continuam fazendo referência para os mesmos

d4 = copy.deepcopy(d1) #fazendo uma cópia profunda