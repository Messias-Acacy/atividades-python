#from math import hypot
#cateto_adj = float(input('digite o valor do cateto adjascente: '))
#cateto_ops = float(input('digite o valor do cateto oposto: '))
#hipotenusa = hypot(cateto_adj,cateto_ops)
#print(f'O valor da hipotenusa desse triângulo é: {hipotenusa:.2f}')

#minha maneira de resolver:
from math import sqrt, pow
cateto_adj = float(input('digite o valor do cateto adjascente: '))
cateto_ops = float(input('digite o valor do cateto oposto: '))
hipotenusa = sqrt(pow(cateto_adj, 2)+pow(cateto_ops,2))
print(f'O valor da hipotenusa desse triângulo é: {hipotenusa:.2f}')