class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        prices = [float('inf')] * n
        prices[src] = 0

        for source, dest, price in flights:
            adj[source].append((price, dest)) # weight, destination

        q = deque([(0, src, 0)]) # price, dest, stops

        while q:
            p, d, s = q.popleft()

            if s > k:
                continue

            for p2, d2 in adj[d]:
                nextCost = p + p2
                if nextCost < prices[d2]:
                    prices[d2] = nextCost
                    q.append((nextCost, d2, s + 1))

        return prices[dst] if prices[dst] != float('inf') else -1