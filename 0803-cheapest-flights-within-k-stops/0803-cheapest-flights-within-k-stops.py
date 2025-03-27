class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        prices = [float('inf')] * n
        prices[src] = 0

        for source, destination, cost in flights:
            adj[source].append((destination, cost)) # node, weight
        
        q = deque([(0, src, 0)]) # (cost, destination, stops)

        while q:
            cost, destination, stops = q.popleft()

            if stops > k:
                continue
            
            for destination2, cost2 in adj[destination]:
                newCost = cost + cost2
                if newCost < prices[destination2]:
                    prices[destination2] = newCost
                    q.append((newCost, destination2, stops + 1))
        

        return prices[dst] if prices[dst] != float('inf') else -1