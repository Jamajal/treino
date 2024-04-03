""" 
    For + Range
    range -> range(start, stop, stop)
"""
    
numeros = range(10)
# numeros = range(5, 10)
# numeros = range(5, 10, 2)
print(numeros)

for numero in numeros:
    print(numero)
print('-------------------')
numeros1 = range(5, 10)
for numero in numeros1:
    print(numero)
print('-------------------')    
numeros2 = range(5, 10, 2)
for numero in numeros2:
    print(numero)


'''
for é uma alternativa de comando de laço de repetição, contudo ele é menos livre do que o while.
Nele basicamente vc define que irá percorrer todas as posições da sequência e também define uma variável para representar a posição de cada 
iteração.

No exemplo acima, no primeiro for estamos percorrendo a sequência numeros, onde cada posição é chamada de numero e podemos realizar coisas
com essa variável no escopo de código do for.

A função range é utilizada para criar uma sequência numérica.
Podemos passar alguns parâmetros para configurar a sequência.

range(10) = uma sequência numérica de 0 a 9

range(5, 10) = uma sequência numérica de 5 até 9.

range(0, 10, 2) = uma sequência numérica de 0 a 9 indo de 2 em 2.

'''