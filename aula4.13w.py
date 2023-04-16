n1= int(input('digite aqui  o primeiro valor: '))
n2= int(input('digite aqui  o segundo valor: '))
while n2 == 0:
    print('só aceitamos valores diferentes de zero para o segundo valor: ')
    n2= int(input('digite aqui  o segundo valor: '))
divisao = n1/n2
print(f'a divisão entre esses dois números é: {divisao}')