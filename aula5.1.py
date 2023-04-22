contador = 0
while contador < 11:
    print(contador)
    contador = contador +1

print(20*'=','usando o for agora')

for x in range(0,11,1):
    print(x)

print(20*'=','usando o for agora')

for x in range(10,-1,-1):
    print(x)

print(20*'=',' usando while agora')

contador = 11
while contador > 0:
    contador = contador - 1
    print(contador)