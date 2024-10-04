class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.first = None
        self.last = None

    def __len__(self):
        return self.size

    def enqueue(self, data):
        node = Node(data)
        if self.size == 0:
            self.first = node
            self.last = node

        else:
            self.last.next = node
            self.last = node

        self.size += 1

    def dequeue(self):
        if self.first != None:
            node = self.first
            self.first = self.first.next
            self.size -= 1
            return node



    def peek(self):
        if self.first != None:
            return self.first.data

    def olhar(self):
        o = ""
        pointer = self.first
        while pointer != None:
            o = o + str(pointer.data) + "->"
            pointer = pointer.next
        return o


fila = Queue()


fila.enqueue(6)
fila.enqueue(2)
fila.enqueue(9)
fila.enqueue(1)

print(fila.olhar())
