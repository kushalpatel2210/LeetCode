from collections import Counter 

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = 0
        res = float('-inf')
        result = ''
        nums = []

        for r in range(len(num)):
            nums.append(num[r])

            if r - l + 1 < 3:
                continue
            
            numString = "".join(nums)
            if len(Counter(numString)) == 1:
                if int(numString) > res:
                    res = int(numString)
                    result = numString

            del nums[0]
            l += 1
        
        return result