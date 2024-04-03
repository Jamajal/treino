"""  
    split e join com list e str
    split - divide um string
    join - une uma string
"""

frase = '   Olha só que    ,   coisa interessante            '
lista_frases_cruas = frase.split(',')
print('1 -', lista_frases_cruas)

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
   lista_frases.append(lista_frases_cruas[i].strip())
   
print('2 -', lista_frases)

frases_unidas = '-'.join(lista_frases)
print('3 -', frases_unidas)

frases_unidas = ', '.join(lista_frases)
print('4 -', frases_unidas)

try:
    lista = ['1', '2', '3', 4]
    numeros_unidos = ''.join(lista)
    print('5 -', numeros_unidos)
except:
    print('Não é possível unir uma numeros')

'''
A função join faz o oposto da função split, você une uma lista em uma string, concatenando as posições. É possível 
definir algum caractere que você queira acrescentar na junção de um posições, com a sintaxe acima.
'''