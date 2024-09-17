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
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
    3: 'avc'
}

print(p1.get('nome'))
print(p1.get(3)) #get retorna o valor da chave colocado de argumento caso a chave existir, caso a chave não exista retorna None

nome = p1.pop('nome') #apaga e retorna o valor da chave de argumento
print(nome)

print(p1)

p1.popitem() #apaga a última chave do dicionário
print(p1)

print(p1)

p1.update({ #atualiza e cria chaves novas
  'nome' : 'Matheus',
  'sobrenome' : 'Kenji',
  'idade' : 21
})

print(p1)

p1.update(nome = 'novo valor', idade = 30)
print(p1)

tupla = ('nome', 'novo valor tupla'),
p1.update(tupla)
print(p1)