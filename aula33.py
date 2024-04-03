""" 
Imutáveis que vimos: str, int, float, bool
"""

string = 'adriano'
# string[3] = 'a' # não permitido

nova_string = f'{string[:3]}ABC{string[4:]}'
print(string.capitalize())
print(string.upper())
print(nova_string)
print(nova_string.zfill(20))

'''
Explicação do código:
nova_string = f'{string[:3]}ABC{string[4:]}'. Primeiro extraimos os 3 primeiros caracteres da variavel string, 
concatenamos com ABC e por fim concatenamos com o quarto caractere em diante.

A função capitalize coloca o primeiro caractere em uppercase.

A função upper coloca todos os caracteres em uppercase.

A função zfill é utilizada para preencher com 0s a esquerda até o comprimento especificado.
'''