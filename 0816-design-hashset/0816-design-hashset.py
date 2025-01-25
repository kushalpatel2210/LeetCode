class MyHashSet:

    def __init__(self):
        self.hashSet = set()

    def add(self, key: int) -> None:
        self.hashSet.add(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        return True if key in self.hashSet else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)