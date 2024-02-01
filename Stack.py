class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self, data=None):
        if not data:
          self.head = data
        else:
          self.head = Node(data);

    def push(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def is_empty(self):
        return(not self.head)

    def pop(self):
        if self.is_empty():
          print("Empty Stack")
          return
        popped = self.head
        self.head = self.head.next
        return popped.data

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def peek(self):
        print("Empty Stack") if self.is_empty() else print(self.head.data)

    def size(self):
      num = 0
      temp = self.head
      while temp:
        num += 1
        temp = temp.next
      return num

    def clear(self):
      self.head = None