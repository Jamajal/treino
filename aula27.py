# 012345678
# Olá mundo
#-987654321
variavel = 'Olá mundo'
print('1 -', variavel[5])
print('2 -', variavel[-4])
print('3 -', variavel[4:])
print('4 -', variavel[4:7])
print('5 -', variavel[:4])
print('6 -', len(variavel))
print('7 -', variavel[0:len(variavel):1])
print('8 -', variavel[0:3:1])
print('9 -', variavel[0:len(variavel):2])
print('10 -', variavel[::-1])
print('11 -', variavel[-1:-10:-1])

'''
Começa a contar as posições a partir do 0. De forma que na string 'Olá mundo', o primeiro caractere, ou seja, a posição variavel[0] é o 'O'.
Se utilizar o sinal de negativo é contado a string de trás pra frente, de forma que -1 é o último caractere da string.
Ao utilizar o :, vc especifica dois números, o da esquerda é onde começa e o da direita é o primeiro caractere que não será incluindo.
De forma que [4:7] indica que você está selecionando do caractere 4 (quinto caractere) até o 6 (sétimo caractere).
'''