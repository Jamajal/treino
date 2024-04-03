condicao = True

if condicao:
    print('Este é o código do if')

print('Fora do if')

if condicao:
    print('Este é o código do if')
else:
    print('Não será executado se condicao for verdadeiro')
    
if 10 == 10:
    print('Outro if')

print('Fora do if')

condicao1 = True
condicao2 = False
condicao3 = False
condicao4 = False

# condicional encadeada
if condicao1:
    print('Código para a condição 1')
elif condicao2:
    print('Código para a condição 2')
elif condicao3:
    print('Código para a condição 3')
elif condicao4:
    print('Código para a condição 4')
else:
    print('Nenhuma condição foi satisfeita')    
    
# condicional aninhada
if condicao1:
    if condicao2:
        print('se condicao 1 e 2 atendidas')
    else:
        print('a condicao 1 atendida e a 2 não')