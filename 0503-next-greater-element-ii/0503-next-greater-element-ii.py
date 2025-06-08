class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [] # (num, idx)
        res = [-1] * n

        for i in range(2 * n):
            num = nums[i % n]

            while stack and stack[-1][0] < num:
                _, idx = stack.pop()
                res[idx] = num

            if i < n:
                stack.append((num, i))
        
        return res