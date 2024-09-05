"""
split e join com list e str
split - divide uma string (list)
join - une uma string
"""

frase = 'Olha só, olha lá'
frases_cortadas_no_espaco = frase.split() #retorna uma lista de palavras cortadas no caractere passado de argumento(OBS: o caractere não será incluído na frase)
print(frases_cortadas_no_espaco)

for i, frase in enumerate(frases_cortadas_no_espaco):
  print(frases_cortadas_no_espaco[i].strip()) #strip corta os espaços da string


frases_unidas = '-'.join(frases_cortadas_no_espaco) #join une uma lista com o elemento que chama esse método
print(frases_unidas)