"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[4:]) #pega o caractere a partir do índice 4 e vai até o fim
print(variavel[4:7]) #pega do índice 4 até antes do índice 7
print(variavel[:4]) #pega do começo até antes do índice 4

print(len(variavel)) #len retorna a quantida de caracteres da str
print(variavel[0:9:2]) #vai do começo e pega os caracteres de 2 em 2