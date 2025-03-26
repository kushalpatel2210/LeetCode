from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for src, dst, time in times:
            adj[src].append((time, dst))

        shortest = {}
        maxTime = float('-inf')
        minHeap = [(0, k)] # (time, dest)

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            
            shortest[n1] = t1
            maxTime = max(maxTime, t1)

            for t2, n2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, n2))
                
        for i in range(1, n + 1):
            if i not in shortest:
                return -1 
        
        return maxTime