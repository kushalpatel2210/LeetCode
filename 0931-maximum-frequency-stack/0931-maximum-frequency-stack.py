class FreqStack:
    
    def __init__(self):
        self.heap = []
        self.cnt = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        heapq.heappush(self.heap, (-self.cnt[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.cnt[val] -= 1
        return val

''''
from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.stack = []
        self.tempStack = []
        self.hashMap = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.hashMap[val] += 1

    def pop(self) -> int:
        maxValue = max(self.hashMap.values())
        maxElements = [key for key, val in self.hashMap.items() if val == maxValue]

        for i in range(len(self.stack) - 1, -1 ,-1):
            if self.stack[i] in maxElements:
                maxFrq = self.stack.pop(i)
                self.hashMap[maxFrq] -= 1
                return maxFrq
'''

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()