class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.cap = capacity
        self.start, self.end = ListNode(), ListNode()
        self.start.next, self.end.prev = self.end, self.start
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.end.prev, self.end
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node) # remove 
            self.insert(node) # insert
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) # remove
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        # cap
        if len(self.cache) > self.cap:
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)