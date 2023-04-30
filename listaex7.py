n = int(input('digite o número que percorre o vetor: '))

a = []
b = []
c = []

for x in range (n):
    a.append(int(input(f'digite o {x+1} valor de a: ')))
    b.append(int(input(f'digite o {x+1} valor de b: ')))

for ad in range (n):
    c.append(a[ad]+b[ad])

print(f'a soma é igual a: {c}')
if c[n-1]%2 != 0:
    print('números pares abaixo: ')
    print('-----')
    for z in range (n):
        if c [z]%2 == 0:
            print(c[z], end=' ')
    print()
    print('-----')
c = []

for sub in range(n):
    c.append(a[sub]-b[sub])
print(f'a subtração é igual a: {c}')

c = []

for mult in range(n):
    c.append(a[mult]*b[mult])
print(f'a multiplicador é igual a: {c}')

c = []

print('a lista c está vazia:',c)