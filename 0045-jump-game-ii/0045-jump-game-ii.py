class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            
            minJump = float('inf')
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                minJump = min(minJump, 1 + dfs(j))
                    
            memo[i] = minJump
            return minJump

        return dfs(0)
