class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = dict()

        def backtrack(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                if backtrack(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        
        return backtrack(0)