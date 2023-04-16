
sexo = 'nada'
rb = 0
if sexo !='M' or sexo !='F':
  while rb ==0:
        sexo = input('digite M ou F: ').strip().upper()[0]
        if sexo =='M' or sexo =='F':
            rb = rb+1
print (f'O seu sexo é: {sexo}')

#sexo = input('digite o sexo aqui: ').strip().upper()[0]
#while sexo not in 'MmFf':
#    sexo = input('digite o sexo aqui: ').strip().upper()[0]
#print(f'{sexo}')
