frase = 'O Python é uma linguagem ' \
    'de programação multiparadigma. ' \
        'Python foi criado por ' \
            'Guido van Rossum.'
            
print(frase.count('o'))

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
letras_que_ja_apareceram = []

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if letra_atual not in letras_que_ja_apareceram: # Acrescentando esse código para não repetir letras 
        qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
        letras_que_ja_apareceram.append(letra_atual)
        
        if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
            qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
            letra_apareceu_mais_vezes = letra_atual
        
        print(letra_atual, qtd_apareceu_mais_vezes_atual)
    i += 1
else:
    print("Letra que apareceu mais vezes:")
    print(letra_apareceu_mais_vezes, qtd_apareceu_mais_vezes)

'''
Explicação do código:
Esse código percorre uma frase informando a quantidade de vezes que cada letra da frase se repete 
e calculando qual a letra que mais se repete.

Observação: 
Python é uma linguagem multiparadigma, ou seja, ela tem aspectos de diversos paradigmas de programação, sendo eles:
Programação Procedural: Python permite escrever programas seguindo o paradigma procedural, onde o código é organizado 
em procedimentos ou funções que realizam operações sequenciais.

Programação Orientada a Objetos (POO): Python suporta totalmente a programação orientada a objetos, permitindo a 
definição e manipulação de classes e objetos, encapsulamento, herança, polimorfismo e outros conceitos relacionados a objetos.

Programação Funcional: Embora não seja tão puramente funcional quanto algumas linguagens como Haskell ou Lisp, Python oferece 
suporte a programação funcional com recursos como funções de ordem superior, funções lambda, compreensão de listas, map, 
reduce, filter, entre outros.

Programação Orientada a Aspectos (POA): Embora não seja nativamente suportada, é possível implementar programação orientada a aspectos em Python usando bibliotecas como AspectLib ou Pyccuracy.

Programação Baseada em Eventos: Python é comumente usado para programação baseada em eventos, especialmente em ambientes 
de interface gráfica de usuário (GUI) e em aplicações web, onde é usado em conjunto com frameworks como Flask, Django e Tkinter.
'''