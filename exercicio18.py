from math import cos, tan, sin, radians
numero = float(input('digite o número em graus aqui:'))
numero_r = radians(numero)

print(f'O cosseno desse número é {cos(numero_r):.2f}\nO seno é {sin(numero_r):.2f} \nE sua tangente é: {tan(numero_r):.2f}')