# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo): #checa se um objeto tem um determinado "Nome" dentro dele
    print('Existe upper')
    print(getattr(string, metodo)()) #getattr retorna o método
else:
    print('Não existe o método', metodo)