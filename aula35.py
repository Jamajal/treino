
# mais sobre while, break e continue 

contador = 0

while contador <= 10:
    contador += 1
    
    print(contador)
    
    if contador == 4:
        break;  # interrompe o programa
    

'''
Dentro de laços de repetição, existem os comandos break e continue.
O break é utilizado para sair da função de repetição e dar sequência no código.
O continue faz com que o programa interrompa a iteração atual e vá para a próxima iteração, mas continua no laço de repetição.
'''

condicao = True
contador = 0

while condicao:
    contador += 1

    print('Entrou aqui')

    if contador == 10:
        break

    if contador >= 0:
        continue

    print('Também entrou aqui')

'''
Note que a condição do while nunca é alteralda, então só é possível sair do laço de repetição através do break que será executado quando
o contador atingir 10.

Note também, que como a primeira coisa que acontece no laço é o incremento do contador, ele sempre será maior que 0, logo o segundo print 
nunca é executado, pois há um continue que pula para a próxima interação. 
'''
