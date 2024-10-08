import importlib #módulo para recarregar os módulos novamente

import aula38_m

print(aula38_m.variavel)

for i in range(10):
  importlib.reload(aula38_m)