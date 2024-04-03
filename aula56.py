"""  
    split e join com list e str
    split - divide um string
    join - une uma string
"""

frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split()
print(lista_palavras)

lista_palavras = frase.split(',')
print(lista_palavras)

lista_palavras = frase.split(', ')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i])
    
for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].strip())    #rstrip() lstrip()

frase = '************Olha só que * coisa interessante**********'
print(frase.strip('*'))

'''
O enumerate é uma boa maneira de trabalhar com o index, neste exemplo temos o valor de cada posição armazenado no i.

split: O split é utilizado para transformar uma string em lista e você pode passar por parâmetro o critério que irá definir as posições.
Caso o critério que você esteja usando resulte em espaços em brancos a esquerda ou a direita em alguma posição, a função strip é 
utilizada para remover espaços em brancos nas extremidades ou caracteres passados por parâmetro.
'''