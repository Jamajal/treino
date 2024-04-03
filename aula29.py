# try/except

print(1234)
print(456)
# int('a')

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

'''
Try e except são importantíssmos quando estamos trabalhando em aplicações que não podem parar de rodar. Eles servem para você fornecer uma 
alternativa de execução caso seu código possua algum erro.

O try vc informa o que você quer que o python tente executar, se não ocorrer nenhum problema, o código será executado
e o except não será executado.

Se houver algum problema do try, nada daquele código é executado e o bloco de código do except é executado.
'''