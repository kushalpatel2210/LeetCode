class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0: # because nums is sorted
                break

            if i > 0 and num == nums[i - 1]:
                continue
                            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                currSum = num + nums[l] + nums[r]

                if currSum == 0:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    l += 1
        
        return res

'''
# backtracking but inefficient
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        nums.sort()

        def backtrack(index, currPath, total):
            if len(currPath) == 3 and total == 0:
                res.append(currPath.copy())
                return

            if index >= len(nums):
                return

            currElement = nums[index]
            currPath.append(currElement) #append
            backtrack(index + 1, currPath, total + currElement) #explore
            currPath.pop()
            

            while index < len(nums) and nums[index] == currElement:
                index += 1

            backtrack(index, currPath, total)

        backtrack(0, [], 0)

        return res
'''