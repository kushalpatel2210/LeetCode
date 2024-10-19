class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second: 
                second = num
            else:
                return True
        
        return False

        '''
        # Using Dp -> but it times out
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    if LIS[i] == 3:
                        return True
        
        return False
        '''