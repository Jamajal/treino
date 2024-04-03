""" 
Lista em Python
Tipo list = Mutável

"""

string = 'ABCDE' 

# lista = list() 
# lista = [];
# print(lista, type(lista))
# print(bool(lista))  #falsy

lista = [123, True, 'Adriano', 1.2, [10]]
print('1 -', lista)

print('2 -', lista[3])
lista[-3] = "Maria"
print('3 -', lista)
print('4 -', lista[2], type(lista[2]))
print('5 -', lista[-1][0])
del lista[1]
print('6 -', lista)
lista.append(50)
print('7 -', lista)
lista.append(60)
lista.append(70)
print('8 -', lista)
print('9 -', lista)
ultimo_valor = lista.pop()
print('10 -', lista, 'Removido ', ultimo_valor)

lista.clear()
print('11 -', lista)

lista.insert(0, 'Adriano')
print('12 -', lista)

lista.insert(100, 'Maria')
print('13 -', lista)

lista.insert(100000, 'Maria')
print('14 -', lista)

lista_a = [1,2,3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print('15 -', lista_c)
lista_d = lista_a.extend(lista_b)
print('16 -', lista_d)
print('17 -', lista_a)
print('18 -', lista_b)

'''
Comandos que podemos executar em uma lista:
append: é usado para adicionar um elemento ao final de uma lista.
pop: é usado para remover e retornar o elemento em um determinado índice da lista. Esse item pode ser atribuido a uma variável.
clear: é usado para remover todos os elementos de uma lista, deixando-a vazia.
insert: é usado para inserir um elemento em uma posição específica da lista.
extend: é usado para adicionar os elementos de uma ao final da lista de outra. Retorna vazio por isso que lista_d recebeu None.
+: usado para concatenar duas listas, criando uma nova lista que contém todos os elementos das listas originais.
'''