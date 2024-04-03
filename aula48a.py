nome = 'Luiz'
nome = 'João'

print('1 -', nome)

lista_a = ['Luiz', 'João', 1, True, 1.2]
lista_b = lista_a

print('2 -', lista_a)
print('3 -', lista_b)

lista_a[0] = 'Adriano'

print('4 -', lista_a)
print('5 -', lista_b)

lista_b = lista_a.copy()
print('6 -', lista_a)
print('7 -', lista_b)

lista_a[0] = 'Thomas'

print('8 -', lista_a)
print('9 -', lista_b)

'''
É possível copiarmos os valores de uma lista de nois modos.
Através da atribuição lista1 = lista2, esse modo faz com que lista2 aponte para o endereço de memória de lista1, logo, as alterações 
feitas em lista 1, refletem em lista2. 
lista2 = lista1.copy(), esse modo copia apenas o conteúdo e as alterações em lista1 não refletem em lista2.
'''