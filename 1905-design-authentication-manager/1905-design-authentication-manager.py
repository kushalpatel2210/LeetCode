import heapq

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.hashMap = dict()
        self.minHeap = [] # (expirationTime, key)

    def generate(self, tokenId: str, currentTime: int) -> None:
        tokenExpiration = currentTime + self.ttl
        self.hashMap[tokenId] = tokenExpiration
        heapq.heappush(self.minHeap, (tokenExpiration, tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hashMap:
            tokenExpiry = self.hashMap[tokenId]
            if tokenExpiry > currentTime:
                tokenNewExpiry = currentTime + self.ttl
                self.hashMap[tokenId] = tokenNewExpiry
                heapq.heappush(self.minHeap, (tokenNewExpiry, tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        while self.minHeap and self.minHeap[0][0] <= currentTime:
            expiry, tokenId = heapq.heappop(self.minHeap)
            if self.hashMap[tokenId] == expiry:
                del self.hashMap[tokenId]
        return len(self.hashMap)

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)