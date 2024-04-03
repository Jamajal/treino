# Operadores lógicos 
# and or not

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
# Avaliação de curto circuito
print(True and False and True)

print(not not True) # os not se anulam
    

'''
o and compara o lado esquerdo e o lado direito, se ambos forem True ele retornará True, senão False
o not retorna o contrário do lado direito dele, se for algo True, passará a ser False.
'''