texto = 'Python'

i = 0

tamanho_string = len(texto) # Essa linha de código é desnecessária, pois essa variável só é usada uma vez
while i< tamanho_string:
    print(texto[i])
    
    i += 1
    

# Códigos idênticos, porém com uma operação a menos
    
texto = 'Python'
i = 0    

while i < len(texto): 
    print(texto[i])
    
    i += 1