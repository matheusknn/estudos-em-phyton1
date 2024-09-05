"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal #usar quando é necessário precisão total dos números

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
nuumero_3 = numero_1 + numero_2
print(nuumero_3)
print(f'{nuumero_3:.2f}')
print(round(nuumero_3, 2)) #round serve para arredondar os números

