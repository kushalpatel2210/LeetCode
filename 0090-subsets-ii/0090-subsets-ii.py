class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        def backtrack(index, currPath):
            res.add(tuple(currPath.copy()))
            
            for i in range(index, n):
                currPath.append(nums[i]) #include
                backtrack(i + 1, currPath) #explore
                currPath.pop() #does not include
        
        nums.sort()
        backtrack(0, [])
        return [list(s) for s in res]