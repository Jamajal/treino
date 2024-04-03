""" 
    Repetições
    while(enquanto)
"""
condicao = True
while condicao:
    print(1)
    print(2)
    print(3)
    condicao = input("Tecle [ENTER] \
        para terminar ou 1 para continuar!")
    
'''
A função while, primeiramente, verifica se a condição é verdadeira, enquanto ela for verdadeira ela irá repetir o bloco de código 
especificado. Quando a condição for falsa o programa sairá da função.

Nesse exemplo, a função while executará pelo menos uma vez, pois a condição foi setada como true, ao final do bloco de código o usuário
pode dar um novo valor para a condição, se ele quiser quebrar o loop do while ele só precisa apertar ENTER, pois como vimos anteriormente, 
uma string vazia equivale a False.
'''