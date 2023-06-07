numero_i = 0
numero_f = 0
numero = input()
numero_i,numero_f = numero.split()

contador_primo = 0
contador_negativo = 0
anterior = 0


for numero in range(int(numero_i),int(numero_f)+1,1):
    contador_primo = 0
    for x in range(1,numero+1):
        if numero % x == 0 and numero != 1:
            contador_primo+=1
        
    if contador_primo == 2:
        

            for y in range(numero,1,-1):
                if y != numero:
                    contador_negativo = 0
                    for h in range(1,numero*2):
                        if h % y == 0 and y != 1 and y%2 != 0 :
                            contador_negativo+=1
                        print(y,h)
                    
                    if contador_negativo == 2:
                        print()
           
                    else:
                        contador_negativo = 0
            
          

    else:
        contador_primo = 0


