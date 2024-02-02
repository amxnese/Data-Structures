class Node():
	def __init__(self,data):
		self.data = data
		self.next = None

class Linked_list():
    def __init__(self):
        self.head = None

    def __str__(self):
        lst = []
        temp = self.head
        while temp:
            lst.append(str(temp.data))
            temp = temp.next
        return " ==> ".join(lst)

    def __len__(self):
            count, temp = 0, self.head
            while temp:
                temp, count = temp.next, count+1
            return count
            
    def Add_at_Begining(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def Add_at_End(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode

    def insert(self,data,index):
        assert index >= 0 and index <= len(self), "index out of range"
        if index == 0:
            self.Add_at_Begining(data)
            return
        newNode = Node(data)
        temp = self.head
        count = 1
        while count != index:
            temp = temp.next
            count += 1
        nxt = temp.next
        temp.next = newNode
        newNode.next = nxt
        
    def Add_to_Empty(self,data):
        if self.is_empty():
            self.head = Node(data)
            return
        print("List Not Empty!")

    def Del_at_Begining(self):
        if self.is_empty():
            print("Empty List!")
            return
        self.head = self.head.next

    def Del_at_End(self):
        if self.is_empty():
            print("Empty List")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def Del_by_Value(self,value):
        if self.is_empty():
            print("Empty List!!")
            return
        if self.head.data == value:
            self.Del_at_Begining()
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if not temp.next:
            print("Value Not in List!")
        else:
            temp.next = temp.next.next

    def is_empty(self):
        return not self.head

    def display(self):
        if self.is_empty():
            print("Empty List")
            return
        temp = self.head
        while temp:
            print(temp.data,end="  ==>  ")
            temp = temp.next
        print("None")

    def Reverse(self):
        if self.is_empty():
            print("Empty List!")
            return
        if not self.head.next:
            pass
        else:
            prv,cur,nxt = self.head,self.head.next,self.head.next.next
            prv.next = None
            while nxt:
                cur.next = prv
                prv,cur,nxt = cur,nxt,nxt.next
            cur.next = prv
            self.head = cur