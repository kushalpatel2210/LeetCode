class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        isIncreasing = nums[0] <= nums[n - 1]
        
        for i in range(1, n):
            if isIncreasing:
                if nums[i] < nums[i -1]:
                    return False
            else:
                if nums[i] > nums[i- 1]:
                    return False
        
        return True

'''
Time Complexity = O(nlogn)
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        sortedAsc, sortedDesc = sorted(nums), sorted(nums, reverse = True)
        return True if nums == sortedAsc or nums == sortedDesc else False
'''