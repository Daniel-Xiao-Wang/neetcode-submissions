class MyQueue:

    def __init__(self):
        self.mystack1 = []
        self.mystack2 = []
        

    def push(self, x: int) -> None:
        self.mystack1.append(x)


    def pop(self) -> int:
        if not self.mystack2:
            while self.mystack1:
                self.mystack2.append(self.mystack1.pop())
        
        return self.mystack2.pop()
        

    def peek(self) -> int:
        if not self.mystack2:
            while self.mystack1:
                self.mystack2.append(self.mystack1.pop())
        
        return self.mystack2[-1]
        

    def empty(self) -> bool:
        return (len(self.mystack2) == 0 and len(self.mystack1) == 0)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()