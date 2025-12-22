class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < len(nums) and j < k:
                target = 0 - num
                curr_sum = nums[j] + nums[k]
                if curr_sum > target:
                    k -= 1
                elif curr_sum < target:
                    j += 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        
        return res