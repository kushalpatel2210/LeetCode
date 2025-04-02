class ListNode():
    def __init__(self, tokenId='', expiryTime=0):
        self.tokenId, self.expiryTime = tokenId, expiryTime
        self.next = self.prev = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.authManager = dict()  # tokenId -> reference to node
        self.start, self.end = ListNode(), ListNode()
        self.start.next, self.end.prev = self.end, self.start  # Link dummy nodes
        self.size = 0
        self.ttl = timeToLive

    def insert(self, node):
        prev, end = self.end.prev, self.end
        prev.next, end.prev = node, node
        node.prev, node.next = prev, end
        self.size += 1

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        self.size -= 1
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        expiry = currentTime + self.ttl
        self.authManager[tokenId] = ListNode(tokenId, expiry)
        self.insert(self.authManager[tokenId])

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.authManager:
            node = self.authManager[tokenId]
            if node.expiryTime > currentTime:
                # Remove node from current position
                self.remove(node)
                # Update expiry time
                node.expiryTime = currentTime + self.ttl
                # Reinsert at the end
                self.insert(node)
            else:
                # If expired, remove from map
                self.remove(node)
                del self.authManager[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        start = self.start.next

        while start != self.end and start.expiryTime <= currentTime:
            self.remove(start)
            del self.authManager[start.tokenId]  # Also remove from dictionary
            start = start.next  # Move to the next node
        
        return self.size

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)