class Node():
	def __init__(self,data):
		self.data = data
		self.ref = None
class Linked_list():
    def __init__(self):
        self.head = None
    def __str__(self):
        return "a linked list module created to demonstrate the perception of the data structure"
    def __len__(self):
            x,temp = 0,self.head
            while temp is not None:
                temp,x = temp.next,x+1
            return int(x)
    def is_empty(self):
        return self.head is None
    def display(self):
        if self.is_empty():
            print("linked list is empty")
        else:
            displayer = self.head
            while displayer:
                print(displayer.data,end="  ==>  ")
                displayer = displayer.next
    def Add_at_Begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def Add_at_End(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            del temp
    def insert(self,data,index):
        assert index <= len(self), "index out of range"
        new_node = Node(data)
        if index == 0:
            self.Add_at_Begining(data)
        else:
            count,temp = 1,self.head
            while temp.next and count != index:
                temp,count = temp.next,count+1
            new_node.next,temp.next= temp.next,new_node
    def Add_to_Empty(self,data):
        if self.is_empty():
            self.head = Node(data)
        else:
            print("linked list is not empty")
    def Del_at_Begining(self):
        if self.is_empty():
            print("linked list is empty")
        else:
            temp = self.head
            self.head = self.head.next
            del(temp)
    def Del_at_End(self):
        if self.is_empty():
            print("linked list is empty")
        elif len(self) == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    def Del_by_Value(self,value):
        if self.is_empty():
            return "linked list is empty"
        elif self.head.data == value:
            print(f"value ==> ({self.head.data}) has been deleted")
            self.Del_at_Begining()
        else:
            temp = self.head
            while temp.next:
                if temp.next.data == value:
                    break
                temp = temp.next
            if temp.next:
                print(f"value ==> ({temp.next.data}) has been deleted")
                d = temp.next
                temp.next = temp.next.next
                del d
            else:
                print(f"value {value} not found")
    def Reverse(self):
        if self.is_empty():
            print("linked list is empty")
        elif not self.head.next:
            return self.head
        else:
            prv,cur,nxt = self.head,self.head.next,self.head.next.next
            prv.next = None
            while nxt:
                cur.next = prv
                prv,cur,nxt = cur,nxt,nxt.next
            cur.next = prv
            self.head = cur