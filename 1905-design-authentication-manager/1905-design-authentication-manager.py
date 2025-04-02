import heapq

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.authManager = dict() # tokenId, expiry
        self.minHeap = [] #(expiryTime, tokenId)
        self.ttl = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        tokenExpiry = currentTime + self.ttl
        self.authManager[tokenId] = tokenExpiry
        heapq.heappush(self.minHeap, (tokenExpiry, tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.authManager:
            currExpiryOfToken = self.authManager[tokenId]
            if currExpiryOfToken > currentTime:
                newExpiry = currentTime + self.ttl
                self.authManager[tokenId] = newExpiry
                heapq.heappush(self.minHeap, (newExpiry, tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.minHeap and self.minHeap[0][0] <= currentTime:
            expiry, tokenId = heapq.heappop(self.minHeap)
            if tokenId in self.authManager and self.authManager[tokenId] <= currentTime:
                del self.authManager[tokenId]
        
        return len(self.authManager)

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)