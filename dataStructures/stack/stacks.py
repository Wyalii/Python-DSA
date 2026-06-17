class Stack:
    def __init__(self)-> None:
        self.items:list[any] = []
        pass
    def push(self,item:any) -> None:
        self.items = self.items + [item]
        pass
    def size(self)->int:
        return len(self.items)
    def pop(self) -> any:
        if len(self.items) == 0:
            return None
        
        i = len(self.items) -1
        removedItem = self.items[i]
        self.items = self.items[:i]
        return removedItem
    
    def peek(self) -> any:
        i = len(self.items) - 1
        return self.items[i]

    

s = Stack()
s.push(10)
s.push(40)
s.push(50)
s.push(60)
s.push(70)
print(s.peek())
s.pop()
print(s.peek())


