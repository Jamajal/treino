lista = ['Maria', 'Helena', 'Luiz']

indices = range(len(lista))

print(indices)

for indice in indices:
    print(indice, lista[indice], type(indice)) # Boa soluçao para se trabalhar com índices sem o enumerate.

for nome in lista:
    print(nome, type(nome))

