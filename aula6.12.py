vetor_a = []
contador_par = 0
menor = 0
maior = 0
numero = 0
somador = 0
contador_maior = 0
for x in range(30):
    vetor_a.append(int(input(f'digite o {x+1} número aqui: ')))

print(20*'-')

for par in range(30):
    if vetor_a[par]%2 == 0:
        contador_par+=1
print(f'a quantidade de números pares é de: {contador_par}')

print(20*'-')

# parte que calcular o maior e o menor
for z in range(30):
    if numero == 0:
        menor = vetor_a[z]
        maior = vetor_a[z]
    numero = 1
    if vetor_a[z] > maior:
        maior = vetor_a[z]
    if vetor_a[z] < menor:
        menor = vetor_a[z]
print(f'o maior valor é: {maior} e o menor valor é: {menor}')

print(20*'-')

for soma in range(30):
    somador = somador + vetor_a[soma]
media = somador/(soma+1)
print(f'a média é igual a: {media}')

print(20*'-')

for h in range (30):
    if vetor_a[h] > (media):
        contador_maior+=1
print(f'existe um total de {contador_maior} valores maior que a média')
