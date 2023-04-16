n = int(input('digite aq: '))
soma = 0
contador = 0
for c in range(1,7):
    n = int(input(f'digite o {c} número: '))
    if n%2 ==0:
        soma = soma+n
        contador = contador +1   
print(f'soma  dos {contador} números pares que você me informou é {soma}')



