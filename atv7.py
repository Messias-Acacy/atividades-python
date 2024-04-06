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


for x in range(10):
    fila.enqueue(x+1)


for x in range(fila.size()):
    pilha.push(fila.dequeue())


for x in range(pilha.size()):
    fila.enqueue(pilha.pop())






