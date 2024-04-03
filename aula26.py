# String formatada

variavel = 'ABC'
print(f'1 - {variavel}')
print(f'2 - {variavel: >10}')
print(f'3 - {variavel: <10}.')
print(f'4 - {variavel: ^10}.')
print(f'5 - {variavel:Ç^10}.')
print(f'6 - {1000.43234234234234:0=+10,.1f}')
print(f'7 - O hexadecimal de 1500 é { 1500:08X}')
#conversion flags
print(f'8 - {variavel!r}') # Forma padrão
print(f'9 - {variavel!s}') # Transforma a variavel em uma string
print(f'10 - {variavel!a}') # Escapa esses caracteres especiais de modo que a string possa ser reproduzida de forma literal e segura

lista = [1, 2, 3, 4] # Criando uma lista que contem números em cada posição
print(f'11 - {lista!s}') # Print a lista como se ela fosse uma string