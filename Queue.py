class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None

    def __len__(self):
      temp, num = self.head, 0
      while temp:
        temp, num = temp.next, num+1
      return num

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

' The Least The Value The Highest The Priority '
class PriorityQueue(Queue): 
    def __init__(self):
        super().__init__()
        self.head = None

    def enqueue(self, data):
        newNode = Node(data)
        # Handling The Case Where The Queue is Empty
        if self.is_empty():
          self.head = newNode
          return
        # Handling The Case Where The New Element Has The Highest Priority
        if self.head.data > data:
          newNode.next = self.head
          self.head = newNode
          return

        prv = self.head
        temp = prv.next 
        '''if The Queue Contain Only One Element temp Will Be None, 
        That's Why We'll Check That it's Not None in The While Loop'''
        while temp and temp.next and temp.data < data:
          prv = prv.next
          temp = temp.next
          
        'Now We Need To Know Why We Broke Out of The Loop'
        
        # The Case Where We Reached The End of The Queue And The New Element Has The Least Priority
        if temp and not temp.next and temp.data < data:
            temp.next = newNode
        
        # The Case Where The New Element Found a Place in The Middle of The Queue
        else:
          prv.next = newNode
          newNode.next = temp