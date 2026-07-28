class MinStack:

    def __init__(self):
        self.stack = []        
        self.minVal=[]

    def push(self, value: int) -> None:
        if not self.minVal:
            self.minVal.append(value)
        else:
            self.minVal.append(min(value,self.minVal[-1]))
        return self.stack.append(value)
        

    def pop(self) -> None:
        self.minVal.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minVal[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()