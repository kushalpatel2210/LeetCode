import random

class RandomizedSet:

    def __init__(self):
        self.hashMap = dict() # val -> idx in nums
        self.nums = list()

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.hashMap[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False
        idx = self.hashMap[val]
        last = self.nums[-1]
        self.hashMap[last] = idx
        self.nums[idx] = last
        self.nums.pop()
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()