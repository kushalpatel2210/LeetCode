class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(currentPath, index):
            res.append(currentPath[:])

            for i in range(index, len(nums)):
                currentPath.append(nums[i]) #include
                backtrack(currentPath, i + 1) # explore
                currentPath.pop() # exclude
        
        backtrack([], 0)
        return res