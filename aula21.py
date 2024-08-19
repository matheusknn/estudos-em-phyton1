# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

nome = 'Matheus'
print(nome[1])
print(nome[-6])
print('a' in nome) #confere se 'a' está dentro da string nome e retorna um boolean
print('the' in nome) #true
print('the' not in nome) #verifica se 'the' não está na string nome e retorna um boolean, nesse caso retorna false pois 'the' está na string nome

nome_digitado = input('Digite um nome: ')
string_que_deseja_encontrar = input('Digite a string que deseja encontrar: ')

if string_que_deseja_encontrar in nome_digitado:
  print(f'{string_que_deseja_encontrar} está dentro do nome {nome_digitado}')
else:
  print(f'{nome_digitado} não possui a string {string_que_deseja_encontrar}')  