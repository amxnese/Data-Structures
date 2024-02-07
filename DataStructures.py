class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prv = None
        self.right = None
        self.left = None
        self.duplicate = 1


class Circular_DLL(Doubly_Linked_list):
    def __init__(self):
        self.head = None
    def __str__(self):
        return "a Circular doubly linked list created by amine"
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
            print("linked list is empty")
        else:
            print(self.head.data,end="  ==>  ")
            displayer = self.head.next
            while displayer != self.head:
                print(displayer.data,end="  ==>  ")
                displayer = displayer.next
        print()
    def r_display(self):
        if self.is_empty():
            print("linked list is empty")
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
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.prv = temp
            newNode.next = self.head
            self.head.prv = newNode
            self.head = newNode
            del temp
    def Add_at_End(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.head.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = newNode
            self.head.prv = newNode
            newNode.next = self.head
            newNode.prv = n
            del n
    def Del_at_Begining(self):
        if self.is_empty():
            print("linked list is empty")
        else:
            headN = self.head.next
            tail = self.head.prv
            self.head.prv = None
            self.head.next = None
            self.head = headN
            tail.next = self.head
            self.head.prv = tail
            del headN,tail
    def Del_at_End(self):
        if self.is_empty():
            print("linked list is empty")
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
            del temp,tmp
    def Del_by_Value(self, value):
        if self.is_empty():
            return "linked list is empty"
        elif self.head.data == value:
            print(f"value ==> ({self.head.data}) has been deleted")
            self.Del_at_Begining()
        else:
            temp = self.head
            while temp.next != self.head:
                if temp.next.data == value:
                    break
                temp = temp.next
            if temp.next != self.head:
                print(f"value ==> ({temp.next.data}) has been deleted")
                d = temp.next
                t = d.next
                t.prv = temp
                temp.next = t
                d.next,d.prv = None,None
                del d,t
            else:
                print(f"value {value} not found")
    def Reverse(self):
        if self.is_empty():
            print("linked list is empty")
        elif self.head.next == self.head:
            return self.head
        else:
            cur = self.head
            nxt = self.head.next
            while nxt != self.head:
                cur.next = cur.prv
                cur.prv = nxt
                cur = nxt
                nxt = nxt.next
            self.head = cur
            t = self.head.next
            self.head.next = self.head.prv
            self.head.prv = t
class Binary_Search_Tree():
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def insert(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.data == data:
                    temp.duplicate+=1
                    break
                elif temp.data > data:
                    if temp.left:
                        temp = temp.left
                    else:
                        temp.left = newNode
                        break
                elif temp.data < data:
                    if temp.right:
                        temp = temp.right
                    else:
                        temp.right = newNode
                        break
    def get_min(self):
        if self.is_empty():
            print("binary tree is empty")
        else:
            temp = self.head
            while temp.left:
                temp = temp.left
            print(temp.data)
    def get_max(self):
        if self.is_empty():
            print("binary tree is empty")
        else:
            temp = self.head
            while temp.right:
                temp = temp.right
            print(temp.data)
    def find(self,value):
        if self.is_empty():
            print(f"value {value} not found")
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    break
                elif temp.data > value:
                    temp = temp.left
                else:
                    temp = temp.right
            if temp:
                print(f"value {value} has been found")
            else:
                print(f"value {value} not found")
    def exists(self,value):
        if self.is_empty():
            return False
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    break
                elif temp.data > value:
                    temp = temp.left
                else:
                    temp = temp.right
            if temp:
                return True
            else:
                return False
    def delete(self,value):
        if self.is_empty():
            print(f"value {value} not found")
        elif self.head.data == value:
            if not self.head.right and not self.head.left:
                self.head = None
                print(f"value {value} deleted")
            elif self.head.right:
                temp = self.head.right
                temp1 = self.head
                while temp.left:
                    if temp.left:
                        temp1 = temp
                    temp = temp.left
                temp2 = temp
                self.head.data = temp.data
                if temp.right:
                    if temp1 != self.head:
                        temp1.left = temp.right
                    else:
                        temp1.right = temp.right
                else:
                    if temp1 != self.head:
                        temp1.left = None
                    else:
                        temp1.right = None
                del temp2
                print(f"value {value} deleted")
                print(f"self.head = {self.head.data}")
            elif self.head.left:
                temp = self.head.left
                temp1 = self.head
                while temp.right:
                    if temp.right:
                        temp1 = temp
                    temp = temp.right
                temp2 = temp
                self.head.data = temp.data
                if temp.left:
                    if temp1 != self.head:
                        temp1.right = temp.left
                    else:
                        temp1.left = temp.left
                else:
                    if temp1 != self.head:
                        temp1.right = None
                    else:
                        temp1.left = None
                del temp2
                print(f"value {value} deleted")
        else:
            if not self.exists(value):
                print(f"value {value} not found")
            else:
                temp = self.head
                while not temp.left.data == value and not temp.right.data == value:
                    if temp.data > value:
                        temp = temp.left
                    else:
                        temp = temp.right
                if temp.right:
                    if temp.right.data == value:
                        if not temp.right.right and not temp.right.left:
                            print(f"value {temp.right.data} deleted")
                            temp.right = None
                        elif not temp.right.right and temp.right.left:
                            print(f"value {temp.right.data} deleted")
                            temp.right = temp.right.left
                        elif temp.right.right and not temp.right.left:
                            print(f"value {temp.right.data} deleted")
                            temp.right = temp.right.right
                        else:
                            temp1 = temp.right.left
                            temp.right = temp.right.right
                            temp2 = temp.right
                            while temp2.left:
                                temp2 = temp2.left
                            print(f"value {temp.right.data} deleted")
                            temp2.left = temp1
                if temp.left:
                    if temp.left.data == value:
                        if not temp.left.left and not temp.left.right:
                            print(f"value {temp.left.data} deleted")
                            temp.left = None
                        elif not temp.left.left and temp.left.right:
                            print(f"value {temp.left.data} deleted")
                            temp.left = temp.left.right
                        elif temp.left.left and not temp.left.right:
                            temp.left = temp.left.left
                        else:
                            temp1 = temp.left.right
                            temp.left = temp.left.left
                            temp2 = temp.left
                            while temp2.right:
                                temp2 = temp2.right
                            print(f"value {temp.left.data} deleted")
                            temp2.right = temp1
    def inorder_traversal(self,start:Node):
        if start:
            self.inorder_traversal(start.left)
            print(start.data)
            self.inorder_traversal(start.right)
    def preorder_traversal(self,start:Node):
        if start:
            print(start.data)
            self.preorder_traversal(start.left)
            self.preorder_traversal(start.right)
    def postorder_traversal(self,start:Node):
        if start:
            self.postorder_traversal(start.left)
            self.postorder_traversal(start.right)
            print(start.data)
class Max_Heap():
    def __init__(self):
        self.head = None
        self.list = []
    def insert(self,data):
        if data not in self.list:
            self.list.append(data)
            while(self.list[(self.list.index(data)-1)//2] < self.list[self.list.index(data)]):
                parent = (self.list.index(data)-1)//2
                current = self.list.index(data)
                temp = self.list[parent]
                self.list[parent] = self.list[current]
                self.list[current]  = temp
                if self.list.index(data) == 0:
                    break
    def delete(self,data):
        if data not in self.list:
            print(f"value {data} not found")
        else:
            if self.list:
                if self.list[self.list.index(data)] == self.list[-1]:
                    self.list.remove(data)
                else:
                    self.list[self.list.index(data)] = self.list[-1]
                    ndata = self.list[-1]
                    self.list.pop(-1)
                    while max(self.list[self.list.index(ndata)],
                    self.list[(self.list.index(ndata)*2)+1],
                    self.list[(self.list.index(ndata)*2)+2])!= self.list[self.list.index(ndata)]:
                        temp = self.list[self.list.index(ndata)]
                        max1 = max(self.list[(self.list.index(ndata)*2)+1],
                        self.list[(self.list.index(ndata)*2)+2])
                        self.list[self.list.index(ndata)] = max1
                        if max1 == self.list[(self.list.index(ndata)*2)+1]:
                            self.list[(self.list.index(ndata)*2)+1] = temp
                        elif max1 == self.list[(self.list.index(ndata)*2)+2]:
                            self.list[(self.list.index(ndata)*2)+2] = temp
    def dislay(self):
        for i,n in enumerate(self.list):
            print(f"{i} ==> {n}")
    def getMax(self):
        return self.list[0]
