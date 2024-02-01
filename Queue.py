class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.is_empty():
          self.head = newNode
          return
        temp = self.head
        while temp.next:
          temp = temp.next
        temp.next = newNode

    def dequeue(self):
        if self.is_empty():
          print("Empty Queue!!")
          return
        print(f"Dequeued {self.head.data}")
        self.head = self.head.next

    def is_empty(self):
        return(not self.head)

    def size(self):
      temp, num = self.head, 0
      while temp:
        temp, num = temp.next, num+1
      return num

    def peek(self):
        print(self.head.data)

    def clear(self):
      self.head = None

    def display(self):
        if self.is_empty():
            print("Empty Queue!!")
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next