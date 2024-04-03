""" 
    For + Range
    range -> range(start, stop, step)
"""

texto = 'Luiz'.__iter__()
print(texto)

texto1 = iter('Adriano')
print(texto1)

print(texto1.__next__())
print(texto1.__next__())
print(texto1.__next__())
print(texto1.__next__())

print('-----------------')
texto2 = iter('Adriano')
print(next(texto2))
print(next(texto2))
print(next(texto2))
print(next(texto2))

numeros = range(0, 100, 8)

for numero in numeros:
    print(numero)


# for letra in texto3
texto3 = 'Neia'
iterator = iter(texto3)

while True:
    try:
        letra = next(iterator)
        print(letra)
    except StopIteration:
        break


for letra in texto3:
    print(letra)
    
'''
Uma maneira de iterar sobre sequências é a utilização do comando iter.
Há comandos que fazem a iteração avançar, como __next__() ou next()
'''