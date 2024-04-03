# Operadores lógicos 
# and or not

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E'or entrada == 'e') and \
#     senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')
    
# Avaliação de curto circuito
senha = input('Senha: ')
if not senha:
    print('Você não digitou nada')

print(not 1)
print(not True)
print(not False)


'''
Como dito anteriormente, o not retorna o contrário do lado direito dele, se for algo True, passará a ser False.
Por isso que:
not 1 = False
not True = False
not False = True
not senha = Se a senha existir indica False, se existir indica True. Esse tipo de verificação é popular para verifica ausência de dados que 
são necessários existir.
'''