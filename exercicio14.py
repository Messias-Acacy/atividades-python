temperatura_c = float(input('digite o valor da temperatura em celsius: '))
#por conta da ordem de procedencia, é possivel realizar o calculo sem os parenteses (nesse caso)
calculo = temperatura_c/5*9+32
#calculo = ((temperatura_c/5)*9)+32
print(f'a temperatura em fahrenheit é: {calculo:.2f}F')