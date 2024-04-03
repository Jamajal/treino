"""
Flag Bandeira - Marcar um local
None = não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

# v1 = 'a'
# v2 = 'a'
# v3 = 'b'

# print(id(v1))
# print(id(v2))
# print(id(v3))

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True # flag
    print('Falso algo')
else:
    print('Não faça algo')
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

'''
O operador is verifica se as duas coisas sendo comparadas tem o mesmo endereço de memória e não se elas tem o mesmo valor
Exemplo:
'''

lista = [1, 2, 3]
lista_2 = [1, 2, 3]
lista_3 = lista

print('1 -', lista is lista_2)
print('2 -', lista is lista_3)

'''
É interessante observar que esse comportamento não acontece pros tipos de dados primitivos, pois o python otimiza o armazenamento de memória
para valores iguais para estes tipos de dados.
'''

nome = 'Pedro'
nome_2 = 'Pedro'
nome_3 = nome

print('3 -', nome is nome_2)
print('4 -', nome is nome_3)