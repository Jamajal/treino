#debug
#settings > glyph margin

import random

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição verdadeira')

condicao_aleatoria = random.randint(0, 1)
if condicao_aleatoria:
    print('Condição aleatória verdadeira')
else:
    print('Condição aleatória falsa')

'''
Como gerar um valor booleano aleatório:
random é um biblioteca que nos concede diversas funções para interagir com aleatoriedade.
randint é uma função de random que gera um número aleatório entre os parâmetros passados, nesse caso o número ou será 0 ou será 1
O Python entende que:
0 = False 
1 = True 
Por isso esse código gera uma variável booleano aleatória na prática.
'''