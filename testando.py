valor = int(input('digite um valor aqui'))
contador1= 0
contador2 = 0
for c in range (1,valor+1,1):
    numero = int(input(f'Digite o {valor} valor:'))
    if numero > 9 and numero < 21: #intervalo de 10 a 20, incluindo 10 e 20
        contador1 += 1
    else:
        contador2 = contador2+1
print(f'A quantidade de números dentro do intervalo foi de: {contador1} e fora do intervalo foi de: {contador2}, {c}')