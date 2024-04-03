# condicionais
# if = se condição for verdadeira, executa bloco de código
# elif = senão se condição for verdadeira, executa bloco de código
# else = senão, executa bloco de código

# if e elif necessitam de uma condição

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('Você saiu do sistema')
    
    print('ok')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')


'''
Explicação das condições:
Se a condição do if for verdadeira executa print('Você entrou no sistema') e ignora todo o resto das verificações. 
Se não verifica se a condição do elif é verdadeira, se for print('Você saiu do sistema') e ignora o resto das verificações. 
Senão, executa print('Você não digitou nem entrar e nem sair.').
'''