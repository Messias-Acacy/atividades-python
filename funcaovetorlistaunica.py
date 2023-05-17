def funcao_unica(argumento):
    resolucao = []
    for x in range(len(argumento)):
        if argumento[x] not in resolucao:
            resolucao.append(argumento[x])
    return resolucao

a = [1,4,4,2,7,8,0,7,2,9]
print(funcao_unica(a))