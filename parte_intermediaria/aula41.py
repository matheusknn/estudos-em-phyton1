# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#   a = x #variável livre = não está definida no corpo da função dentro, ou seja, dentro da função dentro a é variável livre

#   def dentro():
#     print(locals())
#     print(dentro.__code__.co_freevars)
#     return a
#   return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
  valor_final = string_inicial

  def interna(valor_a_concatenar):
    nonlocal valor_final #faz o python buscar a variável em um escopa superior
    valor_final += valor_a_concatenar
    return valor_final
  return interna

c = concatenar('a')
print(c('b'))