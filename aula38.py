
# mais sobre while, break e continue 
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('Acabou')

'''
Quando há um laço de repetição dentro do outro, chamamos de laços aninhados. 
O funcionamento dessa mecânica é o seguinte, começamos com a iteração do primeiro laço, assim que o segundo for chamado, todas as iterações 
do segundo acontecem, antes de dar sequência na iteração do primeiro. Quando o segundo terminar a execução é dado sequência no código do primeiro. 
Esse mesmo processo acontece novamente nas próximas iterações do primeiro laço.

Por exemplo:
Suponha que temos um while que é executado duas vezes, as únicas coisas que ele faz é printar "Primeiro laço" e chamar um outro while. 
O segundo while é executado quatro vezes e apenas printa "Segundo laço".

Dessa forma as mensagens no terminal seriam assim:
Primeiro laço
Segundo laço
Segundo laço
Segundo laço
Segundo laço
Primeiro laço
Segundo laço
Segundo laço
Segundo laço
Segundo laço
'''