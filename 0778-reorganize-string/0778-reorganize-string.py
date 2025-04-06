import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        maxHeap = [(-frq, val) for val, frq in counter.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            frq, char = heapq.heappop(maxHeap)
            frq += 1
            res += char

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if frq != 0:
                prev = (frq, char) 
        
        return res

