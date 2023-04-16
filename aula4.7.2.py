numero = int(input('Digite um número aqui: '))
if numero > 0 :
    for c in range(1,numero+1):
            print(c)
else:
    while numero <= 0:
        numero=int(input('digite um número diferente  ou maior que de zero: '))
    for c in range(1,numero+1):
        print(c)

#numero=int(input('digite um número aqui: '))
#while numero <= 0:
#        numero=int(input('digite um número diferente  ou maior que de zero: '))
#for c in range(1,numero+1):
#    print(c)