""" 
Lista em Python
Tipo list = Mutável

"""

string = 'ABCDE'  # len()
lista = [123, True, 'Adriano', 1.2, []]
print(lista, type(lista))
print(bool(lista)) # falsy
print(lista)
print(lista[2], type(lista[2]))
print(lista[2].upper(), type(lista[2]))

lista[-3]='Maria'
print(lista)

'''
Vimos muitos exemplos de strings sendo tratadado como sequência, contudo existe o tipo list em python.
Ele armazena diversos tipos de dados.
Pode ser uma lista de numeros, strings, valores booleanos, etc. 
Pode até mesmo armazenar diferentes tipos de dados, como exemplificado na linha 8.
É possível acessar uma posição da lista utilizando lista[x], lista é o nome que demos a lista e x é um valor inteiro 
que representa a posição desejada.
'''

