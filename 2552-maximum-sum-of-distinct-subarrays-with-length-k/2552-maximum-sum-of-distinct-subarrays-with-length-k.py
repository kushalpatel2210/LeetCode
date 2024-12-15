class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i = 0
        current_sum = 0
        max_sum = float('-inf')
        distinct_values = set()

        for j in range(len(nums)):
            current_sum += nums[j]
            distinct_values.add(nums[j])

            if j - i + 1 < k:
                continue
            
            if len(distinct_values) == k:
                max_sum = max(current_sum, max_sum)

            # Slide window now 
            current_sum -= nums[i]
            distinct_values.remove(nums[i])
            i += 1
        
        return max(max_sum, 0)

