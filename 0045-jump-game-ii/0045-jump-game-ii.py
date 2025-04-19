class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        
        return res

'''
DP: Top Down 
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
'''