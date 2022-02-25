import math
custoShow = float (input('Preço do show: '))
ingresso = float (input('Preço do ingresso: '))
cobrir = custoShow / ingresso
lucro = 1.23 * custoShow / ingresso
print ('Quantos convites são necessários para cobrir o custo?:', math.ceil(cobrir))
print ('Quantos convites são necessários para lucrar 23%?:', math.ceil(lucro))

