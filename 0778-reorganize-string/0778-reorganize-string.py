class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-frq, char] for char, frq in count.items()]
        heapq.heapify(maxHeap)
        
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            count += 1
            res += char 

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = [count, char]

        return res
