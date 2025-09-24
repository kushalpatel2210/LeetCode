from collections import defaultdict
import random

class RandomizedCollection:

    def __init__(self):
        self.hashMap = defaultdict(set)
        self.nums = list()        

    def insert(self, val: int) -> bool:
        self.hashMap[val].add(len(self.nums))
        self.nums.append(val)
        return len(self.hashMap[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.hashMap[val]:
            return False

        removeIdx = self.hashMap[val].pop()
        lastIdx = len(self.nums) - 1
        lastElement = self.nums[-1]
        self.nums[removeIdx] = lastElement
        self.hashMap[lastElement].add(removeIdx)
        self.hashMap[lastElement].discard(lastIdx)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()