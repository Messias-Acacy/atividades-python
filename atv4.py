
class Stack():
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


pilha = Stack()

def determinarString(x,y,pilha):
    for interable in range(len(x)):
        if(x[interable] == y[len(y)-1-interable]):
            pilha.push(x[interable])
    
    if(pilha.size() == len(x)):
        return True
    else:
        for x in range(pilha.size()):
            pilha.pop()
        return False


print(determinarString("ABCD","DCBA",pilha))


