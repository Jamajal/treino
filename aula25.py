# interpolação
# É o conceito de inserir ou substituir valores dentro de strings

nome = 'Adriano'
preco = 1000.890890
variavel1 = '%s, o preço é R$%.d' % (nome, preco)
variavel2 = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel1)
print(variavel2)

print('O hexadecimal de %d é %02X\n' % (15, 15))

# Exemplo 2
nome = "João"
idade = 30
mensagem = f"Olá, meu nome é {nome} e tenho {idade} anos.\n"
mensagem = "Olá, meu nome é {} e tenho {} anos.\n".format(nome, idade)
print(mensagem)

# Exemplo 3
print(mensagem)

'''
Todos os marcadores de texto do python (Por chatgpt):
%s: Utilizado para interpolar valores de strings.
%d: Utilizado para interpolar valores de inteiros decimais (inteiros).
%f: Utilizado para interpolar valores de números de ponto flutuante.
%x e %X: Utilizado para interpolar valores de inteiros hexadecimais em minúsculas (%x) ou maiúsculas (%X).
%o: Utilizado para interpolar valores de inteiros octais.
%e e %E: Utilizado para interpolar valores de números de ponto flutuante no formato de notação científica em minúsculas (%e) ou maiúsculas (%E).
%g e %G: Utilizado para interpolar valores de números de ponto flutuante em formato compacto em minúsculas (%g) ou maiúsculas (%G).
%i: Utilizado para interpolar valores de inteiros em geral.
%r: Utilizado para interpolar valores de representação "repr" de objetos Python.
'''