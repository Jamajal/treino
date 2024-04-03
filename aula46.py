for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue
    
    if i == 8:
        print('i é 8, seu else não executará')
        break
    
    for j in range(1, 3):
        print(i, j)
        
else:
    print('For completo com sucesso!')
    
'''
Esse código é um bom exemplo da explicação de laços aninhados dado anteriormente.
Note que as execuções do segundo for são executadas todas em sequência antes da próxima iteração do primeiro for acontecer.
'''