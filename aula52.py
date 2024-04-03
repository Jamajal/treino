"""
    tipo tupla - lista imutável
"""

nomes= 'Adriano', 'José', 'Maria'
# nomes[1] = 'Tatiane'
print(nomes)

print(list(nomes), nomes[1])

nova_lista = list(nomes)
print(list(nova_lista), nova_lista[1])
nova_lista[0] = 'André'
print(list(nova_lista), nova_lista[1])
print(list(nomes), nomes[1])

try:
    nomes[1] = 'Leandro'
    print('Posição da tupla alterada')
except:
    print('Tuplas são imutáveis!') # Sempre cairá no except

print(type(nomes))

'''
Caracterísitcas importantes das tuplas:
Tuplas são inicializadas sem []; 
São demarcadas por () no terminal; 
Não podem ter os valores de sua posição alteradas. 
'''