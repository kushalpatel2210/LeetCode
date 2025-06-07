import random

class RandomizedSet:

    def __init__(self):
        self.hashMap = {} # num -> idx
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.hashMap[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False

        indexOfVal = self.hashMap[val]
        lastElement = self.nums[-1]
        self.nums[indexOfVal] = lastElement
        self.hashMap[lastElement] = indexOfVal
        del self.hashMap[val]
        self.nums.pop()
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()