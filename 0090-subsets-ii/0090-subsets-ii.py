class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()

        def backtrack(currPath, index):
            if index == len(nums):
                res.append(currPath.copy())
                return 
            
            currPath.append(nums[index])
            backtrack(currPath, index + 1)
            currPath.pop()

            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            backtrack(currPath, index + 1)
        
        backtrack([], 0)
        return res

'''
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
'''