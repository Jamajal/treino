nome = 'Adriano'
altura = 1.72
peso = 101
imc = peso / (altura)**2

linha_1 = f'{nome} tem {altura:,.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:,.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

print(nome, 'tem', altura, 'de altura,',)
print('peso ', peso, 'quilos e imc de :')
print(imc)