class Pilha():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


pilha = Pilha()
isvalido = False
sequencia = input()

for x in sequencia:
    try:
        if(x == "I"):
            pilha.push(0)
        else:
            pilha.pop()

    except:
        isvalido = False
        break
    isvalido=True

if(pilha.isEmpty() == True):
    if(isvalido == True):
        print("VÁLIDO")
    else:
        print("INVÁLIDO")
else:
    print("INVÁLIDO")
    




