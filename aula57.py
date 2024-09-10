"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

print('verdadeiro' if True else 'falso') #se a condição for verdadeira retorna o primeiro valor e se a condição for falsa retorna o valor depois do else

digito = 10
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)