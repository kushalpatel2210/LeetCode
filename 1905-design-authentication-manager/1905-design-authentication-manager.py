class AuthenticationManager:    
    def __init__(self, time_to_live: int):
        # Initialize the time_to_live for the tokens
        self.time_to_live = time_to_live
        # Use a dictionary to keep track of the tokens and their expiration times
        self.token_expirations = defaultdict(int)

    def generate(self, token_id: str, current_time: int) -> None:
        # Create a new token with an expiration time based on current_time + time_to_live
        self.token_expirations[token_id] = current_time + self.time_to_live

    def renew(self, token_id: str, current_time: int) -> None:
        # Renew a token's expiration time if it hasn't already expired
        if self.token_expirations[token_id] > current_time:
            self.token_expirations[token_id] = current_time + self.time_to_live

    def countUnexpiredTokens(self, current_time: int) -> int:
        # Count the number of tokens that have not yet expired
        return sum(expiration_time > current_time for expiration_time in self.token_expirations.values())
'''
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
'''

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)