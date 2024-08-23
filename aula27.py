"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    quanto mais afastado da margem o código <- Contagem de complexidade (ruim)
"""

velocidade = 61 #velocidade atual do carro
local_carro = 101 #local que o carro está na estrada

#em python n existem constantes, porém, é usado a convensão de tudo em uppercase para identificar essas variáveis
RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 está
RADAR_RANGE = 1 #distância onde o radar pega


if velocidade > RADAR_1:
  print('Carro passou da velocidade do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)and velocidade > RADAR_1:
  print('carro multado em radar 1')