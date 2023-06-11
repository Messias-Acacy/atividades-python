vetor = [5,4,13,2,11,1,688,66,21,8]

for a in range (len(vetor)):
    for x in range(len(vetor)):
        local=x+1
        if local > (len(vetor)-1):
            break
        else:
            if vetor[x] > vetor[local]:
                vetor.insert(x,vetor[local])
                del vetor[x+2]
print(vetor)