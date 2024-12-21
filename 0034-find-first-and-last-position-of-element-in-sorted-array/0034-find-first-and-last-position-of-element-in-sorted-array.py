class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(condition):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if condition(mid):
                    right = mid
                else:
                    left = mid + 1
            return left
    
        # Find the first occurrence of the target
        start = binary_search(lambda mid: nums[mid] >= target)
        
        # If the target doesn't exist in the array
        if start >= len(nums) or nums[start] != target:
            return [-1, -1]
        
        # Find the last occurrence of the target
        end = binary_search(lambda mid: nums[mid] > target) - 1
        
        return [start, end]
