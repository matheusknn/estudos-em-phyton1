""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string): #o else é executado depois do loop do while terminar, se algo quebrar o loop o else não será executado
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')
print('Fora do while.')