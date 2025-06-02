from collections import Counter
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        odd = nums[1::2]
        even = nums[0::2]
        res = 0
        
        oddCounter = Counter(odd)
        evenCounter = Counter(even)
        topOdd = oddCounter.most_common(2)
        topEven = evenCounter.most_common(2)

        if len(topOdd) == 1:
            topOdd.append((None, 0))
        if len(topEven) == 1:
            topEven.append((None, 0))

        if topOdd[0][0] != topEven[0][0]:
            res = n - topOdd[0][1] - topEven[0][1]
        else:
            res = min(n - topOdd[0][1] - topEven[1][1], n - topOdd[1][1] - topEven[0][1])
        
        return res