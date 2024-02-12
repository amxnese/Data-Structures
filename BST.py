class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Binary_Search_Tree():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def insert(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
        else:
            temp = self.head
            while True:
                if temp.data >= data:
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

    def get_min(self,node:Node):
        if not node:
            print("Empty Tree!")
        else:
            temp = node
            while temp.left:
                temp = temp.left
            return temp.data

    def get_max(self, node:Node):
        if not node:
            print("Empty Tree!")
        else:
            temp = node
            while temp.right:
                temp = temp.right
            return temp.data

    def find(self,value):
        if self.is_empty():
            print("Empty Tree!")
        elif self.head.data == value:
            print(f"{value} is The Head of The Tree")
        else:
            path = ""
            temp = self.head
            while temp:
                if temp.data == value:
                    break
                elif temp.data > value:
                    temp = temp.left
                    path += " left"
                else:
                    temp = temp.right
                    path += " right"
            if temp:
                print(f"Path of The Value {value} is: {path}")
            else:
                print(f"Value {value} Not Found")

    def exists(self,value):
        if self.is_empty():
            return False
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    return True
                elif temp.data > value:
                    temp = temp.left
                else:
                    temp = temp.right
            return False

    def delete(self, node:Node, value):
        if not self.exists(value):
          return
        if node.data > value and node.left.data != value:
          self.delete(node.left, value)
        elif node.data < value and node.right.data != value:
          self.delete(node.right, value)
        else:
          if not node.left and not node.right:
            self.head = None
          elif node.data == value:
            temp = self.get_min(node.right)
            node.data = temp
            self.delete(node.right, temp)
          elif node.left.data == value:
            if not node.left.right:
              node.left = node.left.left
            elif not node.left.left:
              node.left = node.left.right
            else:
              temp = self.get_min(node.left.right)
              node.left.data = temp
              if temp == node.left.right.data:
                node.left.right = None
                return
              self.delete(node.left.right, temp)
          elif node.right.data == value:
            if not node.right.left:
              node.right = node.right.right
            elif not node.right.right:
              node.right = node.right.left
            else:
              temp = self.get_min(node.right.right)
              node.right.data = temp
              if temp == node.right.right.data:
                node.right.right = None
                return
              self.delete(node.right.right, temp)

    def inorder_traversal(self,start:Node):
        if start:
            self.inorder_traversal(start.left)
            print(start.data, end="  ")
            self.inorder_traversal(start.right)

    def preorder_traversal(self,start:Node):
        if start:
            print(start.data, end="  ")
            self.preorder_traversal(start.left)
            self.preorder_traversal(start.right)
    def postorder_traversal(self,start:Node):
        if start:
            self.postorder_traversal(start.left)
            self.postorder_traversal(start.right)
            print(start.data, end="  ")