dias_extenso = ('zero','um','dois','três','Quatro','cinco','seis','sete','oito','nove','dez')
dias_atuais = (0,1,2,3,4,5,6,7,8,9,10)
numero = int(input('Digite um número entre 0 e 10: '))
while numero < 0 or numero > 10:
    numero = int(input('Digite um número entre 0 e 10: '))
for x in range(len(dias_extenso)):
    if dias_atuais[x] == numero:
        print(f'Você digitou: {dias_extenso[x]}')
        break

#dias_extenso = ('zero','um','dois','três','Quatro','cinco','seis','sete','oito','nove','dez')
#numero = int(input('Digite um número entre 0 e 10: '))
#while True:
#    print(f'Você digitou {dias_extenso[numero]}')
#    break
