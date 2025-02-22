class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = list()
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.k:
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True
        return False

    def Front(self) -> int:
        return -1 if not self.queue else self.queue[0]

    def Rear(self) -> int:
        return -1 if not self.queue else self.queue[-1]
        
    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()