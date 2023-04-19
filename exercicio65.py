numero = 0
confirm = 'S'
somador = 0
contador = 0
maior = 0
menor = 0
while confirm == 'S':
    numero = int(input('Digite um número inteiro aqui: '))
    somador = somador + numero
    contador = contador + 1
    confirm = input('Quer continuar? Digite S para sim e qualquer outra coisa para não: ').upper().strip()[0]
    if contador == 1:
        maior = somador
        menor = somador
    else:
        if numero > maior:
            maior = numero
        else:
            menor = numero

print(f'Você digitou {contador} valores. A soma entre esses números é {somador}.  a média é: {somador/contador} e o maior valor é {maior} e o menor valor é {menor}')