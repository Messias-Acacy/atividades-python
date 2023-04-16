numero = int(input('digite um número: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cent = numero // 100 % 10
milh = numero // 1000 % 10
print(f"a unidade é: {uni} a dezena é: {dez} a centena é: {cent} a milhar é: {milh}")