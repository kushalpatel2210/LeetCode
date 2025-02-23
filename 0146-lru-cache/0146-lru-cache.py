class Node:

    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key, node

        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left # Connect left and right 
    
    # remove the element
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # inser at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove
            self.remove(self.cache[key])
            # insert at the end
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check if length exceeds or not
        if len(self.cache) > self.cap:
            lru = self.left.next
            # remove from linked list
            self.remove(lru)
            # remove from cache
            del self.cache[lru.key]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)