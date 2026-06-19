class Queue:
    def __init__(self):
        self.items:list[any] = []
        pass
    def push(self,item:any) ->None:
        new_items = []
        for i in range(len(self.items)):
            new_items.append(self.items[i])

        self.items.append(item)
        self.items = new_items    
        pass
    def pop (self) ->any:
       if len(self.items) == 0:
            return None

       removed = self.items[0]
       new_items = []
       for i in range(1,len(self.items)):
           new_items.append(self.items[i])

       self.items = new_items       
       return removed
    def peek(self) -> any:
        if len(self.items) == 0:
         return None
        return self.items[0]
    def size(self)->int:
        return len(self.items)


myQueue = Queue()
myQueue.push(22)
myQueue.push(23)
myQueue.push(25)
myQueue.push(24)
myQueue.push(26)
print(myQueue.peek())