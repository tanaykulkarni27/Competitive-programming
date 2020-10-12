class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def add(self,data):
        self.next = Node(data)
    def print(self,next):
        if next == None:
            return None
        print(next.data)
        return self.print(next.next)
    def total(self, next,s=0):
        if next == None:
            return s
        s+=next.data
        return self.total(next.next,s)
class LinkedList:
    def __init__(self):
        self.Node = None
        self.previous = None
    def add(self,data):
        if self.previous == None:
            self.Node = Node(data)
            self.previous = self.Node
        else:
            self.previous.next = Node(data)
            self.previous = self.previous.next
    def find_total(self):
        if self.Node == None:
            return 'List is blank'
        return self.Node.total(self.Node)
    def print_all(self):
            self.Node.print(self.Node)
list = LinkedList()
list.add(5)
list.add(4)
list.add(3)
list.add(2)
list.add(1)
total = list.find_total()
print(total)
