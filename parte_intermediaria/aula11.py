def criar_multiplicador(multiplicador):
  def multiplicar(numero):
    return numero * multiplicador
  return multiplicar

duplicar = criar_multiplicador(3)
print(duplicar(2))