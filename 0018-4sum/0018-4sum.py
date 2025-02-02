class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = set()

        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                twoSum = num + nums[j]
                l, r = j + 1, len(nums) - 1

                while l < r:
                    four_sum = twoSum + nums[l] + nums[r]

                    if four_sum == target:
                        quadruplets.add((num, nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif four_sum > target:
                        r -= 1
                    else:
                        l += 1
        

        return [list(tpl) for tpl in quadruplets]