class ListNode:
    def __init__(self, val = 0, nxt = None):
        self.val = val
        self.next = nxt

class MyCircularQueue:
    def __init__(self, k: int):
        self.space = k 
        self.left = ListNode()
        self.right = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        
        curr = ListNode(value)
        if self.isEmpty():
            self.left.next = curr
            self.right = curr
        else:
            self.right.next = curr 
            self.right = curr
        
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.left.next = self.left.next.next
        if self.left.next is None:
            self.right = self.left
        
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.val

    def isEmpty(self) -> bool:
        return self.left.next == None

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

'''
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
'''