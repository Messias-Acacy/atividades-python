km = float(input('Quantos Km você rodou com seu carro? '))
dias = float(input('Por quantos dias ele foi alugado? '))
pagamento = (km*0.15)+(dias*60)
print(f'o total de pagamento é igual a {pagamento:.2f} reais')