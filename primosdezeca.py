numero = int(input('digite um número'))
contador_primo = 0

contador_negativo = 0
contador_positivo = 0
contador_zeca = 0

anterior = 0
sucessor = 0


for x in range(1,numero+1):
    
    if numero % x == 0 and numero != 1:
            contador_primo+=1

if contador_primo == 2:
   #negativo
    for z in range(numero,0,-1):
        if z != numero:
            for y in range(z,0,-1):
                if z % y == 0:
                     contador_negativo+=1
            if contador_negativo == 2:
                    anterior = z
                    break          
            else:
                    contador_negativo = 0  

    # positivo
    for h in range(numero,2000):
        if h != numero:
            for a in range(1,h+1,1):
                if h % a == 0:
                    contador_positivo+=1
            if contador_positivo == 2:
                 sucessor = h
                 break
            else:
                 contador_positivo = 0


    if (sucessor+anterior)/2 == numero:
        contador_zeca+=1
        print(f'o número {numero} é zeca! {contador_zeca}')
    else:
         print('não é primo de zeka!')

