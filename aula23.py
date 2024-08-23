"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a  
"""

variavel = 'ABC'
print(f'{variavel: >10}') # > preenche os espços na esquerda de acordo com o número colocado na direita
print(f'{variavel:#>10}') 
print(f'{variavel: <10}')
print(f'{21123312.123213123123123123213:,.3f}')