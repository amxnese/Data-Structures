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
                    self.list.pop()
                    while True:
                        i = self.list.index(ndata)
                        try:
                            mx = max(self.list[i],
                            self.list[i*2+1],
                            self.list[i*2+2])
                        except:
                            mx = max(ndata,
                            self.list[i*2+1])
                        if mx == ndata:
                            break
                        temp = ndata
                        try:
                            max1 = max(self.list[(i*2)+1],
                            self.list[(self.list.index(ndata)*2)+2])
                        except:
                            max1 = self.list[(i*2)+1]
                        tmp = self.list.index(ndata)
                        self.list[i] = max1
                        if max1 == self.list[(i*2)+1]:
                            self.list[(i*2)+1] = temp
                        elif max1 == self.list[(i*2)+2]:
                            self.list[(i*2)+2] = temp
                        if self.list.index(ndata)*2 > len(self.list):
                            break

    def display(self):
        for i,n in enumerate(self.list):
            print(f"{i} ==> {n}")

    def getMax(self):
        return self.list[0]