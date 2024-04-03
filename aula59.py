# Desempacotamento em chamadas
# de métodos e funções

# string = 'ABCD'
# lista = ['Adriano', 'Cristiane', 'Eduarda']
# print(lista)
# tupla = 'Python', 'é', 'legal'
# print(tupla)

# p, q, r = lista;
# print(q)

# lista = ['Adriano', 'Cristiane', 1, 2, 3, 'Eduarda']

# p, q, *_, r = lista;
# print(r)
# print(_)

# print(*lista)
# print(*string)

# for nome in lista:
#     print(nome, end=' ', sep=' ')
    

salas = [
    # 0  1
    ['Maria', 'Helena', ],  #0
    # 0
    ['Elaine',],    #1
    # 0 1 2
    ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40, 50) ],  #2
]

print(salas)
print(*salas)
print(*salas, end='\n', sep='\n')
print(*salas, sep='\n')