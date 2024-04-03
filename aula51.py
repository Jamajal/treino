"""
    Desempacotamento de lista + tuplas
"""

nome1, nome2, nome3 = ['Adriano', 'Maria', 'José']
print(nome1)
print(nome2)
print(nome3)

# nome2, nome3 = ['Adriano', 'Maria', 'José']
# print(nome2)

nome2, *resto = ['Adriano', 'Maria', 'José']
print(nome2)
print(resto)

'''
O código mostra como trabalhar com o operador de resto, tal qual o ... em javascript.
'''