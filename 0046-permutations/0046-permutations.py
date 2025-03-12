class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                res.append(sol.copy())
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res
