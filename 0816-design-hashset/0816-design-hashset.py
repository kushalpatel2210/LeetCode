class MyHashSet:

    def __init__(self):
        self.hashSet = list()

    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashSet else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)