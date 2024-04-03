"""

"""
import decimal 

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print('1 -', numero_3)
print('2 -', f'{numero_3:.2f}')
print('3 -', round(numero_3, 2))


numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
numero_3 = numero_1 + numero_2

print('4 -', numero_3)
print('5 -', f'{numero_3:.2f}')
print('6 -', round(numero_3, 2))

numero_1 = decimal.Decimal('0.1')
numero_2 = decimal.Decimal('0.7')
numero_3 = numero_1 + numero_2

print('7 -', numero_3)
print('8 -', f'{numero_3:.2f}')
print('9 -', round(numero_3, 2))

'''
O valor de numero_3 é representado por 0.7999999999999999 em vez de 0.8, devido a uma limitação na 
representação binária o que pode causar essa imprecisão.

numero_2 = decimal.Decimal(0.7) cria um número decimal que ainda mantem a imprecisão.
numero_2 = decimal.Decimal('0.7') cria um número decimal que não possui imprecisão.
'''