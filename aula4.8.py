#c_t = 0
#c_n = 0
#while b <10:
#    numero = int(input('digite um número aqui: '))
#    c_t= c_t+1
#    if numero<0:
#        c_n=c_n+1 
#print(f' quantidade de número negativos é: {c_n}')

numeros=0
negativos=0
for c in range (1,11):
    numero = int(input('Digite o número aqui: '))
    numeros=numeros+1
    if numero <0:
        negativos=negativos+1
print(f' quantidade de número negativos é: {negativos}')
