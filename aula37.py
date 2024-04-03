
# mais sobre while, break e continue 

contador = 0

while contador <= 10:
    contador += 1
    
    if contador == 2:
        continue  #volta para o início
    
    print(contador)
    
    if contador == 4:
        break;  # interrompe o programa
    