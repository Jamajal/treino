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
senha = input('Senha: ') or 'sem senha' 
print(senha)

'''
Explicação:
O python executa o input ele recebe um valor, se o usuário não digitar nada, ele recebará uma string vazia.
Quando chega no or, o python verificará a condição da esquerda (SEMPRE A DA ESQUERDA PRIMEIRO), se existir algo ele entende como True.
Como or só precisa de que uma das partes seja verdadeira ele ficará com o input informado.
Se for uma string vazia ele entenderá como False e atribuirá o valor da direita a variavel senha, pois o valor da direita é garantido que existe.
'''
    

    