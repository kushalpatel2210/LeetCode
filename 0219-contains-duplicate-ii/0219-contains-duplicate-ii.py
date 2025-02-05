class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = set()
        
        for i in range(len(nums)):
            if nums[i] in numbers:
                return True
            
            numbers.add(nums[i])
            
            if len(numbers) > k:
                numbers.remove(nums[i - k])
        
        return False
