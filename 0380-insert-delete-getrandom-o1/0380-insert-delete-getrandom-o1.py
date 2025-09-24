import random 

class RandomizedSet:

    def __init__(self):
        self.hashMap = {}
        self.numbers = []

    def insert(self, val: int) -> bool:
        if val not in self.hashMap:
            self.numbers.append(val)
            self.hashMap[val] = len(self.numbers) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashMap:
            idx = self.hashMap[val]
            lastNumber = self.numbers[-1]
            self.hashMap[lastNumber] = idx
            self.numbers[idx] = lastNumber
            self.numbers.pop()
            del self.hashMap[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.numbers)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()