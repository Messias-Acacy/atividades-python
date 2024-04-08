class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def printQueue(self):
        for e in self.items:
            print(e,end="->")
        print()


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

fila = Queue()

pilha = Stack()



itens = [1,-1,2,-2,3,-3,4,-4,28,-58,-85]
for x in range(len(itens)):
    fila.enqueue(itens[x])


fila.printQueue()

for x in range(fila.size()):
    numero = fila.dequeue()
    if(numero < 0):
        pilha.push(0)
    else:
        pilha.push(numero)


for x in range(pilha.size()):
    fila.enqueue(pilha.pop())

for x in range(fila.size()):
    pilha.push(fila.dequeue())

for x in range(pilha.size()):
    fila.enqueue(pilha.pop())


fila.printQueue()





    
