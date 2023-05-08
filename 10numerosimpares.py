numero = 0
cont = 0
a = []
while numero != 10:
    if cont %2 != 0:
        a.append(cont)
        numero+=1
    cont+=1
print(a)