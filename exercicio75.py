numero = int(input('digite o primeiro valor: ')),int(input('digite o segundo valor: ')),int(input('digite o terceiro valor: ')),int(input('digite o quarto valor: '))
cont_nove=0

for x in range(len(numero)):
    if numero[x] == 9:
        cont_nove +=1

    
for y in range(len(numero)):
    if numero[y] ==3:
        print(f'O número 3 foi digitado pela primeira  vez na {y} posição')
        break
print('Os números pares são: ')
for z in range(len(numero)):
    if numero[z] %2 ==0 and numero != 0:
        print(numero[z], end=' ')