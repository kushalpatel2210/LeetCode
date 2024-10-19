class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        start, end = 0, len(nums) - 1
        counter = 0

        nums.sort()
        
        while start < end:
            sum = nums[start] + nums[end]
            if sum < k:
                start += 1
            elif sum > k:
                end -= 1
            else: 
                counter += 1
                start += 1
                end -= 1

        return counter
