class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prv = None

class Linked_list():
    def __init__(self):
        self.head = None

    def __str__(self):
        lst = []
        temp = self.head
        while temp:
            lst.append(str(temp.data))
            temp = temp.next
        return ", ".join(lst)

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

class Doubly_Linked_list(Linked_list):
    def __init__(self):
        self.head = None

    def __str__(self):
        lst = []
        temp = self.head
        while temp:
            lst.append(str(temp.data))
            temp = temp.next
        return ", ".join(lst)

    def __len__(self):
        num, temp = 0, self.head
        while temp:
            temp, num = temp.next, num+1
        return num

    def is_empty(self):
        return not self.head

    def display(self):
        if self.is_empty():
            print("Empty List!")
            return
        temp = self.head
        while(temp):
            print(temp.data, " ==> ", end="")
            temp = temp.next
        print("None")

    def Add_at_Begining(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            return
        self.head.prv = newNode
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
        newNode.prv = temp

    def insert(self,data,index):
        assert index >= 0 and index <= len(self), "index out of range!!"
        newNode = Node(data)
        if index == 0:
            self.Add_at_Begining(data)
        elif index == len(self):
            self.Add_at_End(data)
        else:
            temp, count = self.head, 1
            while count != index:
                temp, count= temp.next, count+1
            temp1 = temp.next
            temp.next = newNode
            newNode.next = temp1
            temp1.prv = newNode
            newNode.prv = temp

    def r_display(self):
        if self.is_empty():
            print("Empty List!")
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        while(temp):
            print(temp.data, " ==> ", end="")
            temp = temp.prv
        print("None")

    def Del_at_Begining(self):
        if self.is_empty():
            print("Empty List!")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prv = None if self.head else None

    def Del_at_End(self):
        if self.is_empty():
            print("Empty List!")
        elif len(self) == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            tmp = temp.next
            temp.next = None
            tmp.prv = None

    def Del_by_Value(self,value):
        if self.is_empty():
            return "Empty List!"
        elif self.head.data == value:
            print(f"value ==> ({self.head.data}) has been deleted")
            self.Del_at_Begining()
        else:
            temp = self.head
            while temp.next and temp.next.data != value:
                temp = temp.next
            if temp.next and temp.next.data == value:
                self.Del_at_End()
                return
            elif temp.next:
                print(f"value ==> ({temp.next.data}) has been deleted")
                d = temp.next
                t = temp.next.next
                t.prv = temp
                temp.next = t
                d.next,d.prv = None,None
            else:
                print(f"value {value} not found")

    def Reverse(self):
        if self.is_empty():
            print("Empty List")
        elif not self.head.next:
            return self.head
        else:
            cur = self.head
            nxt = self.head.next
            while nxt:
                cur.next = cur.prv
                cur.prv = nxt
                cur = nxt
                nxt = nxt.next
            self.head = cur
            self.head.next = self.head.prv
            self.head.prv = None

class Circul_SLL(Linked_list):
    def __init__(self):
        super().__init__()
        self.head = None

    def __str__(self):
        if self.is_empty():
            return ""
        lst = []
        temp = self.head
        while True:
            lst.append(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return "".join(str(lst))

    def __len__(self):
        if not self.head:
            return 0
        num ,temp = 1,self.head.next
        while temp != self.head:
            temp,num  = temp.next,num+1
        return int(num)
            
    def display(self):
        if self.is_empty():
            print("Empty List!")
            return
        print(self.head.data, end=" ==> ")
        displayer = self.head.next
        while displayer != self.head:
            print(displayer.data,end=" ==> ")
            displayer = displayer.next

    def Add_at_Begining(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head = newNode

    def Add_at_End(self,data):
        if self.is_empty():
            self.Add_at_Begining(data)
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            
    def Add_to_Empty(self, data):
        if self.is_empty():
            self.Add_at_Begining(data)
            return
        print("List Not Empty!")

    def insert(self, data, index):
        assert index <= len(self), "index out of range"
        new_node = Node(data)
        if index == 0:
            self.Add_at_Begining(data)
        else:
            count,temp = 1,self.head
            while count != index:
                temp,count = temp.next,count+1
            nxt = temp.next
            temp.next = new_node
            new_node.next = nxt

    def Del_at_Begining(self):
        if self.is_empty():
            print("Empty List!")
            return
        if self.head == self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    def Del_at_End(self):
        if self.is_empty():
            print("Empty List!")
        elif len(self) == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next.next = None
            temp.next = self.head

    def Del_by_Value(self, value):
        if self.is_empty():
            return "Empty List!"
        elif self.head.data == value:
            print(f"value ==> ({self.head.data}) has been deleted")
            self.Del_at_Begining()
        else:
            temp = self.head
            while temp.next != self.head and temp.next.data != value:
                temp = temp.next
            if temp.next.next == self.head:
                self.Del_at_End()
            elif temp.next != self.head:
                print(f"value ==> ({temp.next.data}) has been deleted")
                temp.next = temp.next.next
            else:
                print(f"value {value} not found")

    def Reverse(self):
        if self.is_empty():
            print("Empty List!")
        elif self.head.next == self.head:
            return self.head
        else:
            prv,cur,nxt = self.head,self.head.next,self.head.next.next
            tail = prv
            while nxt != self.head:
                cur.next = prv
                prv,cur,nxt = cur,nxt,nxt.next
            cur.next = prv
            self.head = cur
            tail.next = self.head

class Circular_DLL(Doubly_Linked_list):
    def __str__(self):
        if self.is_empty():
            return ''
        lst = [str(self.head.data)]
        temp = self.head.next
        while temp != self.head:
            lst.append(str(temp.data))
            temp = temp.next
        return ", ".join(lst) 

    def __len__(self):
        if self.is_empty():
            return 0
        elif not self.head.next:
            return 1
        else:
            x,temp = 1,self.head.next
            while temp != self.head:
                temp,x = temp.next,x+1
            return int(x)

    def display(self):
        if self.is_empty():
            print("Empty List!")
        else:
            print(self.head.data,end="  ==>  ")
            displayer = self.head.next
            while displayer != self.head:
                print(displayer.data,end="  ==>  ")
                displayer = displayer.next
        print()

    def r_display(self):
        if self.is_empty():
            print("Empty List!")
        elif len(self) == 1:
            print(self.head.data,end="  ==>  ")
        else:
            n = self.head
            while(n.next != self.head):
                n = n.next
            print(n.data,end="  ==>  ")
            n = n.prv
            while(n.next != self.head):
                print(n.data,end="  ==>  ")
                n = n.prv

    def Add_at_Begining(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.head.next = self.head
            self.prv = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.prv = temp
            newNode.next = self.head
            self.head.prv = newNode
            self.head = newNode

    def Add_at_End(self,data):
        if self.is_empty():
            self.Add_at_Begining(data)
        else:
            newNode = Node(data)
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = newNode
            newNode.prv = n
            newNode.next = self.head
            self.head.prv = newNode

    def insert(self,data,index):
        assert index >= 0 and index <= len(self), "index out of range!!"
        newNode = Node(data)
        if index == 0:
            self.Add_at_Begining(data)
        elif index == len(self):
            self.Add_at_End(data)
        else:
            temp, count = self.head, 1
            while count != index:
                temp, count= temp.next, count+1
            temp1 = temp.next
            temp.next = newNode
            newNode.next = temp1
            temp1.prv = newNode
            newNode.prv = temp

    def Add_to_Empty(self, data):
        if self.is_empty():
            self.Add_at_Begining(data)
            return
        print("List Not Empty!")

    def Del_at_Begining(self):
        if self.is_empty():
            print("Empty List!")
        elif self.head == self.head.next:
            self.head = None
        else:
            new_head = self.head.next
            tail = self.head.prv
            self.head.prv = None
            self.head.next = None
            self.head = new_head
            tail.next = self.head
            self.head.prv = tail

    def Del_at_End(self):
        if self.is_empty():
            print("Empty List!")
        elif len(self) == 1:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            tmp = temp.next
            tmp.prv = None
            tmp.next = None
            temp.next = self.head
            self.head.prv = temp

    def Del_by_Value(self, value):
        if self.is_empty():
            return "Empty List!"
        elif self.head.data == value:
            print(f"value ==> ({self.head.data}) has been deleted")
            self.Del_at_Begining()
        else:
            temp = self.head
            while temp.next != self.head and temp.next.data != value:
                temp = temp.next
            if temp.next == self.head:
                raise ValueError(f"{value} Not Found!")
            else:
                print(f"value ==> ({temp.next.data}) has been deleted")
                d = temp.next
                t = d.next
                t.prv = temp
                temp.next = t
                d.next,d.prv = None,None

    def Reverse(self):
        if self.is_empty():
            print("Empty List!")
        elif self.head.next == self.head:
            return
        else:
            cur = self.head
            nxt = self.head.next
            while nxt != self.head:
                cur.next = cur.prv
                cur.prv = nxt
                cur = nxt
                nxt = nxt.next
            self.head = cur
            temp = self.head.next
            self.head.next = self.head.prv
            self.head.prv = temp