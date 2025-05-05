class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
                
            left, right = i + 1, len(nums) - 1

            while left < right:
                currSum = nums[i] + nums[left] + nums[right]

                if currSum == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif currSum > 0:
                    right -= 1
                else:
                    left += 1
        
        return [list(triplet) for triplet in res]