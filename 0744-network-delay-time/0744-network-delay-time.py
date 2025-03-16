from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list) # { source: [(dest, time)]}

        for route in times:
            u, v, time = route 
            adj[u].append((v, time)) #(dest, time)

        shortest = {}
        minHeap = [(0, k)] # (time, k)

        while minHeap:
            curr_time, destination = heapq.heappop(minHeap)

            if destination in shortest and shortest[destination] < curr_time:
                continue
            
            shortest[destination] = curr_time

            for destination2, time2 in adj[destination]:
                if destination2 not in shortest:
                    heapq.heappush(minHeap, (curr_time + time2, destination2))

        if len(shortest) < n:
            return -1
        
        return max(shortest.values())

