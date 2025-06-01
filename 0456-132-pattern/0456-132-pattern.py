class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # mono decreasing # (num, minEle) 
        minEle = nums[0]

        for num in nums:
            while stack and stack[-1][0] <= num:
                stack.pop()
            
            if stack and stack[-1][1] < num:
                return True

            minEle = min(minEle, num)
            stack.append((num, minEle))

        return False