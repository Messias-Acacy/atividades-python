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


filaUm = Queue()
filaDois = Queue()


add = [1,3,5,7,9]

for x in range(len(add)):
    filaUm.enqueue(add[x])

add = [2,4,6,8]

for x in range(len(add)):
    filaDois.enqueue(add[x])

maior = filaUm.size() if filaUm.size() > filaDois.size() else filaDois.size()



if(maior == filaUm.size()):
    contador = filaDois.size()
    for x in range(filaUm.size()):
        n1 = filaUm.dequeue()

        if(contador > 0):
            n2 = filaDois.dequeue()
            if(n1 > n2):
                print(f"{n2} {n1}",end=" ")
                
            else:
                print(f"{n1} {n2}",end=" ")
        

        else:
            print(n1,end=' ')
        contador-=1
else:
    for x in range(filaDois.size()):
        contador = filaUm.size()
        n1 = filaDois.dequeue()

        if(contador > 0):
            n2 = filaUm.dequeue()
            if(n1 >= n2):
                print(f"{n2} {n1}",end=" ")
            else:
                print(f"{n1} {n2}",end=" ")
                

        else:
            print(n1,end=' ')
        contador-=1

        



    

