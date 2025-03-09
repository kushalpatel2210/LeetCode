class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        res = ""
        while maxHeap:
            n = len(res)

            if n < 2:
                count, char = heapq.heappop(maxHeap)
                res += char
                count += 1
                if count:
                    heapq.heappush(maxHeap, (count, char))
            else:
                first, second = res[n - 1], res[n - 2]
                count, char = heapq.heappop(maxHeap)
                
                if first == second == char: 
                    if not maxHeap:
                        break
                    count2, char2 = heapq.heappop(maxHeap)
                    res += char2
                    count2 += 1
                    if count2:
                        heapq.heappush(maxHeap, (count2, char2))   
                    heapq.heappush(maxHeap, (count, char))
                else:
                    res += char
                    count += 1
                    if count:
                        heapq.heappush(maxHeap, (count, char))

        return res  


'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a != 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b != 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c != 0:
            heapq.heappush(maxHeap, (-c, 'c'))
        
        res = ""

        while maxHeap:
            if not maxHeap:
                return res
            n = len(res)
            if n < 2:
                count, char = heapq.heappop(maxHeap)
                res += char
                count += 1
                if count < 0:
                    heapq.heappush(maxHeap, (count, char))
            else:
                first, second = res[n - 1], res[n - 2]
                count, char = heapq.heappop(maxHeap)
                if first != second or not (first == second == char):
                    res += char
                    count += 1
                    if count < 0:
                        heapq.heappush(maxHeap, (count, char))
                elif maxHeap and first == second == char: 
                    count2, char2 = heapq.heappop(maxHeap)
                    res += char2
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(maxHeap, (count2, char2))   
                    if count < 0:
                        heapq.heappush(maxHeap, (count, char))
                else:
                    return res

        return res  
'''