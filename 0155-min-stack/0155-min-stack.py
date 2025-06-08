class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.s2 or self.s2[-1] >= val:
            self.s2.append(val)

    def pop(self) -> None:
        popped = self.s1.pop()
        if self.s2 and self.s2[-1] == popped:
            self.s2.pop()

    def top(self) -> int:
        return self.s1[-1]
        
    def getMin(self) -> int:
        return self.s2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()