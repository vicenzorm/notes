class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.size > 0:
            new_node = self.top
            self.top = self.top.next 
            self.size -= 1
            return new_node.data
        else:
            raise ValueError("Não há valores para serem deletados")


    def peek(self):
        if self.size > 0:
            return self.top.data
        else:
            raise ValueError("Não há valores para serem mostrados")
        

    def olhar(self):
        o = ""
        pointer = self.top
        while pointer != None:
            o = o + str(pointer.data) + "->"
            pointer = pointer.next

        return o



pilha = Stack()
pilha.push(5)
pilha.push(2)
pilha.push(4)
pilha.push(2)
pilha.push(9)



print(pilha.olhar())