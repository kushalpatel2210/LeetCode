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
            print(f"res {res}")
            if n < 2:
                count, char = heapq.heappop(maxHeap)
                res += char
                count += 1
                if count < 0:
                    heapq.heappush(maxHeap, (count, char))
            else:
                first, second = res[n - 1], res[n - 2]
                print(f"inside else first {first} second {second}")
                count, char = heapq.heappop(maxHeap)
                if first != second or not (first == second == char):
                    print("inside if")
                    res += char
                    count += 1
                    if count < 0:
                        heapq.heappush(maxHeap, (count, char))
                elif maxHeap and first == second == char: 
                    print("inside elif")
                    count2, char2 = heapq.heappop(maxHeap)
                    res += char2
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(maxHeap, (count2, char2))   
                    if count < 0:
                        heapq.heappush(maxHeap, (count, char))
                else:
                    print("inside else")
                    return res

        return res  