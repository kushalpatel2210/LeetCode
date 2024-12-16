class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = set()
        
        for i in range(n):
            target = nums[i]
            left = i + 1
            right = n - 1

            # two sum
            while left < right:
                # Process elements 
                currentSum = nums[left] + nums[right]

                # increase or decrease counter 
                if currentSum + target == 0:
                    result.add((target, nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif currentSum + target > 0:
                    right -= 1
                else:
                    left += 1
    
        return [list(ele) for ele in result]