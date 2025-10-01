from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.nums = list()
        self.hashMap = defaultdict(set)         

    def insert(self, val: int) -> bool:
        self.hashMap[val].add(len(self.nums))
        self.nums.append(val)
        return True if len(self.hashMap[val]) == 1 else False

    def remove(self, val: int) -> bool:
        if not self.hashMap[val]:
            return False
        
        lastElementIndex = len(self.nums) - 1
        lastElement = self.nums[-1]
        indexOfVal = self.hashMap[val].pop()
        self.nums[indexOfVal] = lastElement
        self.hashMap[lastElement].add(indexOfVal)
        self.hashMap[lastElement].discard(lastElementIndex)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()