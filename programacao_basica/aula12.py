a = 'A'
b = 'B'
c = 1.1

formato = 'a={0} b={1} c={2:.2f}'.format(a, b, c)
formato2 = 'a={1} b={0} c={2:.2f}'.format(a, b, c) 
formato3 = 'a={A}'.format(A=a, B=b, numero=c)

print(formato)
print(formato2)
print(formato3)