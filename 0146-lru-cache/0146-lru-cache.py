class ListNode: # Doubly linked-list
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.start, self.end = ListNode(), ListNode()
        self.start.next, self.end.prev = self.end, self.start 
    
    def insert(self, node):
        prev = self.end.prev
        prev.next = self.end.prev = node
        node.next, node.prev = self.end, prev
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)