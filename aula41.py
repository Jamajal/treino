string = "valorqualquer"

i = 0
while i < len(string):
    letra = string[i]
    
    if letra == " ":
        break
    
    print(letra)
    i += 1
else:
    print("Laço chegou até o fim")

'''
len retorna o tamanho da sequência que é passado por parâmetro

Esse while é um bom mecanismo de como percorrer sequências, nele podemos ver que a condição é definida por um contador i que começa no 0, 
aumenta conforme a execução do laço e é comparado com o tamanho da string.

Dentro do código usamos o valor de i para exibir a posição da string, e o código será executado até o tamanho da string -1 for executado, pois 
a primeira posição da string é 0, logo a posição string[len(string)] não existe.
'''