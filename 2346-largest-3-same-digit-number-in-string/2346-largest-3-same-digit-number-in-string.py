class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1
        
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                res = max(res, int(num[i]))
                
        return str(res) * 3 if res != -1 else ""

'''
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
'''