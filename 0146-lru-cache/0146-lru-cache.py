class ListNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict() # (key, ref#ListNode)
        self.start, self.end = ListNode(), ListNode()
        self.start.next, self.end.prev = self.end, self.start
    
    # Remove node
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    # insert at the end
    def insert(self, node):
        prev, end = self.end.prev, self.end
        prev.next, end.prev = node, node
        node.prev, node.next = prev, end

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # remove
            self.remove(node)
            # insert
            self.insert(node)
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove        
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove least recently used
            lru = self.start.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)